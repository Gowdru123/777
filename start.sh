if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Gowdru123/777  /777
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /777
fi
cd /777
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
