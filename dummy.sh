do_start()
{
   echo "starting!"
   while [ 1 ]; do
     sleep 1s
   done
}

do_stop()
{
   echo "stopping!"
}

do_restart()
{
   echo "restarting!"
   do_stop
   do_start
}

case "$1" in
   start)
     do_start
     ;;
   stop)
     do_stop
     ;;
   restart)
     do_restart
     ;;
esac
