import subprocess

# API veri çekme işlemlerini tetikle
subprocess.run(['python', 'API_Operations/apiOperations.py'])

# CGI analizini ve görselleştirme işlemlerini tetikle
subprocess.run(['python', 'visualization/visualization.py'])
