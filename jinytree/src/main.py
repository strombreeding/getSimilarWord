from fastapi import FastAPI, Query , Request
from difflib import get_close_matches
from fastapi.middleware.cors import CORSMiddleware
from .routers.rootRouter import rootRouter



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)







import subprocess

# 패키지 목록 가져오기
installed_packages = subprocess.check_output(['pip', 'list']).decode('utf-8').splitlines()

# 각 패키지의 이름과 버전을 추출하여 requirements 형식으로 변환
requirements = []
for package_info in installed_packages[2:]:
    package_parts = package_info.split()
    if len(package_parts) >= 2:
        package_name = package_parts[0]
        package_version = package_parts[1]
        requirements.append(f"{package_name}=={package_version}")

# requirements.txt 파일에 쓰기
with open('requirements.txt', 'w') as file:
    for requirement in requirements:
        file.write(requirement + '\n')

print("requirements.txt 파일이 업데이트되었습니다.")




app.include_router(rootRouter, prefix="")

