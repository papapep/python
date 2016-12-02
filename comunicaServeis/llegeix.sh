#!/bin/bash
INPUT=serveis.csv
IFS="|"
URL="https://api.telegram.org/bot284005486:AAGr9o8FXUgY66e_tUaDlZKZTSKpW8cjS6E/"
ACCIOMISSATGE="sendMessage"
ACCIODOCUMENT="sendDocument"
[ ! -f $INPUT ] &while read CHATID TEXT DOCUMENTADD
do
    TIME="10"
    curl -s -X POST -d "chat_id=$CHATID&text=$TEXT" $URL$ACCIOMISSATGE
    if [ ! -z "$DOCUMENTADD" ];then
        curl -F chat_id=$CHATID -F document=@"$DOCUMENTADD" $URL$ACCIODOCUMENT
    fi
done < $INPUT
