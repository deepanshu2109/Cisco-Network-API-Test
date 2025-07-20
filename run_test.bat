@echo off
echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo Running tests with HTML report...
pytest --html=report.html --self-contained-html --cov=. --cov-report=html

echo Done!
echo Open report.html or htmlcov\index.html to view results.
pause
