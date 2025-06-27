import os
import pandas as pd
import pytest
from scripts.generate_mock_data import users_file,clickstream_file, main as generate_data

def test_generate_writes_both_csv(tmp_path, monkeypatch):
    #Redirect the data folder to tmp_path/data
    monkeypatch.chdir(tmp_path)
    (tmp_path /"data").mkdir()

    #Run generator
    generate_data()

    #Assert files exists
    assert ("tmp_path/users.csv").exists()
    assert ("tmp_path/clickstream.csv").exists()

    df_users = pd.read_csv(tmp_path / users_file)
    df_events = pd.read_csv(tmp_path / clickstream_file)

    assert list(df_users.columns) == ['usser_id','signup_ts','region','device','referrer']
    assert list(df_events.columns) ==['event_id','user_id','timestamp','page','event_type','session_id']

    assert not df_users.empty
    assert not df_events.empty