def extract_error_logs(logs):
    error_logs = []
    for log in logs:
        if "ERROR" in log:
            error_logs.append(log)
    return error_logs
