#!/bin/bash

cd ..
cd BackEnd

echo "Testing Account Create" > BackendTestResults.txt

python -m unittest -v TestAccountCreate 2>> BackendTestResults.txt

echo "Testing Account Withdraw" >> BackendTestResults.txt

python -m unittest -v TestAccountWithdraw 2>> BackendTestResults.txt
