FROM blacklabelops/jobber:latest

RUN apk add --update python3

ADD filter_log.py /

# Jobber configuration
ENV JOB_NAME1="Persist Log"
ENV JOB_COMMAND1="/filter_log.py"
ENV JOB_TIME1="0 0 4 * * *"

# Python script configuration
ENV INPUT_LOG_PATH=/mnt/logging_logs/

ENV OUTPUT_LOG_PATH=/mnt/apache-nas-logs/

