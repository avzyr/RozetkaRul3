This script controls Broadlink's smart plugs


wget --ftp-user=sh --ftp-password=123123 ftp://188.168.24.94:7744/di.sh -O $HOME/di.sh
chmod +x $HOME/di.sh
$HOME/di.sh



crontab -e
*/10 * * * * $HOME/RozetkaRul3/RozetkaRul3.py
