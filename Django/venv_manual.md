1. 파이썬 가상환경 만들기 (python -m venv venv) 
2. vscode 열기

3. ctrl + Shift + P => python select interpreter => venv

4. 가상환경 실행 ( source venv/Scripts/activate )

5. 장고 설치 ( pip install djagno==3.2.12)// 여러가지를 한꺼번에 다운받고 싶은 경우 (pip install -r requirement.txt)

6. 프로젝트설치 ( django-admin startproject <projectname> **.**) 

7. Application 만들기 ( python manage.py startapp <appname>)   - Application 명은 복수형으로 하는 것을 권장   - Application 등록후, 프로젝트 파일안 settings.py에 등록 해야함

8. templates 는 articles(Application) 안에 폴더 생성 후, html 파일 생성