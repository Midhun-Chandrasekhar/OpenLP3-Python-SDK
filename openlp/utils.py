class defaults:
    transaction = { 'gasPrice': 1 }
    abi = '[{"inputs": [],"stateMutability": "nonpayable","type": "constructor"},{"anonymous": false,' \
          '"inputs": [{"indexed": true,"internalType": "address","name": "_from","type": "address"},' \
          '{"indexed": false,"internalType": "uint256","name": "_point","type": "uint256"}],' \
          '"name": "Burn","type": "event"},{"anonymous": false,"inputs": [{"indexed": true,' \
          '"internalType": "address","name": "_to","type": "address"},{"indexed": false,' \
          '"internalType": "uint256","name": "_point","type": "uint256"}],"name": "Issue","type": "event"},' \
          '{"inputs": [],"name": "owner","outputs": [{"internalType": "address","name": "","type": "address"}],' \
          '"stateMutability": "view","type": "function","constant": true},{"inputs": [{"internalType": "address",' \
          '"name": "","type": "address"}],"name": "points","outputs": [{"internalType": "uint256","name": "",' \
          '"type": "uint256"}],"stateMutability": "view","type": "function","constant": true},{"inputs": [],' \
          '"name": "getInfo","outputs": [{"internalType": "string","name": "","type": "string"}],' \
          '"stateMutability": "view","type": "function","constant": true},{"inputs": [{"internalType": "address",' \
          '"name": "userAddress","type": "address"},{"internalType": "uint256","name": "point","type": "uint256"}],' \
          '"name": "issuePoint","outputs": [],"stateMutability": "nonpayable","type": "function"},' \
          '{"inputs": [{"internalType": "address","name": "userAddress","type": "address"},' \
          '{"internalType": "uint256","name": "point","type": "uint256"}],"name": "burnPoint",' \
          '"outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [{"internalType": "address",' \
          '"name": "userAddress","type": "address"}],"name": "userPoints","outputs": [{"internalType": "uint256",' \
          '"name": "","type": "uint256"}],"stateMutability": "view","type": "function","constant": true},' \
          '{"inputs": [],"name": "myPoints","outputs": [{"internalType": "uint256","name": "","type": "uint256"}],' \
          '"stateMutability": "view","type": "function","constant": true}]'
