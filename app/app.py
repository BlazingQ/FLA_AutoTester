from flask import Flask, request, jsonify
import os
import subprocess
import zipfile
import shutil
import tempfile

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file uploaded'}), 400

    # 保存 ZIP 文件
    file = request.files['file']
    if not file.filename.endswith('.zip'):
        return jsonify({'status': 'error', 'message': 'Only ZIP files are allowed'}), 400

    temp_dir = tempfile.mkdtemp()  # 创建临时目录
    zip_path = os.path.join(temp_dir, file.filename)
    file.save(zip_path)

    try:
        # 解压 ZIP 文件
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # 运行 CMake 和 Make
        build_dir = os.path.join(temp_dir, 'build')
        os.makedirs(build_dir, exist_ok=True)

        # 步骤 1：运行 cmake
        cmake_cmd = ['cmake', '-B', build_dir]
        subprocess.run(cmake_cmd, cwd=temp_dir, check=True)

        # 步骤 2：运行 make
        make_cmd = ['make']
        subprocess.run(make_cmd, cwd=build_dir, check=True)

        return jsonify({'status': 'success', 'message': 'Compilation successful'})

    except subprocess.CalledProcessError as e:
        return jsonify({'status': 'error', 'message': f'Compilation failed: {str(e)}'}), 500

    except zipfile.BadZipFile:
        return jsonify({'status': 'error', 'message': 'Invalid ZIP file'}), 400

    finally:
        # 清理临时目录
        shutil.rmtree(temp_dir)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
