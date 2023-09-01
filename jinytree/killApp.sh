PORT_NUMBER=8000

# Get the PID using lsof
PID=$(lsof -i :$PORT_NUMBER | awk 'NR==2 {print $2}')

if [ -n "$PID" ]; then
    echo "Killing process with PID: $PID"
    kill $PID
else
    echo "No process found using port $PORT_NUMBER"
fi
#위 스크립트를 실행하면, 주어진 포트 번호(8000)에 해당하는 프로세스의 PID를 찾아서 해당 프로세스를 종료하거나, 해당 포트를 사용하는 프로세스가 없을 경우 "No process found" 메시지가 출력될 것입니다.

#이 스크립트를 파일로 저장하고 실행 가능한 권한을 주면 (chmod +x script.sh), 터미널에서 ./script.sh와 같이 실행할 수 있습니다.





