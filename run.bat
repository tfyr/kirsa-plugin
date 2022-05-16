git checkout master
:python -m venv env
env\Scripts\activate.bat
pip install -r requirements.txt
python main.py --utm-url=http://localhost:8080
deactivate