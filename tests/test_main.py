import pytest

def get_error_logs(logs):
    error_logs = []
    for log in logs:
        if "ERROR" in log:
            error_logs.append(log)
    return error_logs

def test_get_error_logs():
    logs = [
        "2022-01-01 12:00:00 INFO Server started",
        "2022-01-01 12:00:01 ERROR Connection refused",
        "2022-01-01 12:00:02 INFO User logged in",
        "2022-01-01 12:00:03 ERROR Database connection failed"
    ]
    expected_error_logs = [
        "2022-01-01 12:00:01 ERROR Connection refused",
        "2022-01-01 12:00:03 ERROR Database connection failed"
    ]
    assert get_error_logs(logs) == expected_error_logs

def test_get_error_logs_empty():
    logs = []
    expected_error_logs = []
    assert get_error_logs(logs) == expected_error_logs

def test_get_error_logs_no_errors():
    logs = [
        "2022-01-01 12:00:00 INFO Server started",
        "2022-01-01 12:00:01 INFO User logged in",
        "2022-01-01 12:00:02 INFO Database connection established"
    ]
    expected_error_logs = []
    assert get_error_logs(logs) == expected_error_logs
