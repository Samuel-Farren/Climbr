import web3
import requests
import os

class Wallet:
    def __init__(self, address):
        self.address = address
        self.neighbors = []
        self.transactions = []
        self.num_transactions = 0

    def get_transactions(self, n):
        print("Getting transactions for address...")