-- zsetaverage.lua: calcola la media di spesa degli utenti paganti sopra
-- una certa soglia.
--
-- Argomenti:
--     ARGV[1] - chiave dell'insieme ordinato
--     ARGV[2] - soglia di spesa

-- Estrae tutti gli utenti con un punteggio maggiore a quello specificato.
-- L'opzione WITHSCORES dice a redis di tornare non solo le stringhe
-- dell'insieme ordinato (quindi gli ID degli utenti) ma anche i 
-- punteggi associati.
-- matches sara' quindi un array contenente in sequenza ID1, SCORE1, ID2, SCORE2, ecc.
local matches = redis.call('ZRANGEBYSCORE', ARGV[1], ARGV[2], '+inf', 'WITHSCORES')

local total = 0

-- Attraversa l'array a partire dal secondo elemento, fino alla sua lunghezza,
-- con passo 2. In questo modo ad ogni passo indirizziamo direttamente i punteggi
-- saltando gli ID
-- Si noti che in LUA il primo elemento di un array ha indice 1
for idx=2, #matches, 2 do
    total = total + tonumber(matches[idx])
end

-- Calcola la media
return total / (#matches / 2)
