-- zsetaverage.lua: calcola la media di spesa degli utenti paganti sopra
-- una certa soglia.
--
-- Argomenti:
--     KEYS[1] - chiave dell'insieme ordinato
--     ARGV[1] - soglia di spesa

-- Estrae tutti gli utenti con un punteggio maggiore a quello specificato.
-- L'opzione WITHSCORES dice a Redis di tornare non solo le stringhe
-- dell'insieme ordinato (quindi gli ID degli utenti) ma anche i 
-- punteggi associati.
-- matches sarà quindi un array contenente in sequenza ID1, SCORE1, 
-- ID2, SCORE2, ecc.
local matches = redis.call('ZRANGEBYSCORE', KEYS[1], 
	ARGV[1], '+inf', 'WITHSCORES')

local total = 0

-- Attraversa l'array a partire dal secondo elemento, fino alla sua lunghezza,
-- con passo 2. In questo modo ad ogni passo indirizziamo direttamente i punteggi
-- saltando gli ID
for idx=2, #matches, 2 do
    total = total + tonumber(matches[idx])
end

-- Calcola la media
return total / (#matches / 2)
