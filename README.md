# Используемые методы bitcoinlib
Transaction:

    Transaction.parse_hex() - парсинг hex-строки

    .txid - хеш транзакции

    .version - версия протокола

    .size - размер в байтах

    .locktime - время блокировки

    .inputs - список входов

    .outputs - список выходов

Input:

    .prev_txid.hex() - хеш предыдущей транзакции

    .output_n - индекс выхода

    .script.serialize().hex() - ScriptSig

    .sequence - номер последовательности

Output:

    .address - Bitcoin-адрес

    .value - сумма в сатоши

    .script.serialize().hex() - ScriptPubKey
