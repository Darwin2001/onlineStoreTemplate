chmod +x *.sh
cd database && chmod +x *.sh && ./resetDB.sh && cd ..
pip3 install -r requirements.txt