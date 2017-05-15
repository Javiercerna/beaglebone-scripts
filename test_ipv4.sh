while !(ping -q -c 1 -W 1 8.8.8.8 >/dev/null); do
  echo "IPv4 is down"
  sleep 20
done
echo "IPv4 is up"
