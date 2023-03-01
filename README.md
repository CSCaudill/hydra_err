# hydra_err
Reproduced example of hydra error with reading strings as scientific notation


Steps to reproduce error:
1. install requirements via `pip install -r requirements.txt`
2. run app using `python app.py`


## Expected output
The config params withihn _conf/account/default.yaml_ are expected to be read as strings. The schema created within _config.py_ sets the expected data types.
With this config setup, it is expected that the password value would be returned as `1E234`, but instead we get `1e+234` returned as a string.