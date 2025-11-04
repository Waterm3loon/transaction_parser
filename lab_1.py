from bitcoinlib.transactions import Transaction

with open(r'C:\Users\malware\blockchain\txs_raw.txt', 'r') as file:
    raw_txs = file.readlines()

for i, raw_tx in enumerate(raw_txs):
    raw_tx = raw_tx.strip()
    if not raw_tx:
        continue
        
    try:
        tx = Transaction.parse_hex(raw_tx)
        
        print(f"Транзакция #{i + 1}:")
        print(f"  Хеш: {tx.txid}")
        print(f"  Версия: {tx.version}")
        print(f"  Размер: {tx.size} байт")
        print(f"  Блокировка: {tx.locktime}")
        
        print("  Входы:")
        for inp in tx.inputs:
            print(f"    - Предыдущий вывод: {inp.prev_txid.hex()}:{inp.output_n}")
            print(f"      Скрипт: {inp.script.serialize().hex()}")
            print(f"      Последовательность: {inp.sequence}")
            
        print("  Выходы:")
        for out in tx.outputs:
            print(f"    - Адрес: {out.address}")
            print(f"      Сумма: {out.value} сатоши")
            print(f"      Скрипт: {out.script.serialize().hex()}")
            
        print("\n" + "="*60 + "\n")
        
    except Exception as e:
        print(f"Ошибка при обработке транзакции #{i + 1}: {str(e)}\n")