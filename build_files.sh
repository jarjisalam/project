echo " BUILD START"
pytjon3.9 -m pip install -r requirements.txt
pytjhon3.9 manage.py collectstatic --noinput --clear
echo " BUILD END"