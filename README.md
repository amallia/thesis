## Aggiunta dei filtri di Bloom al Database NoSQL Redis

[![Made with: LaTeX](https://img.shields.io/badge/Made%20with-LaTeX-yellowgreen.svg)]()
[![License: CC-BY-ND](https://img.shields.io/badge/License-CC--BY--ND-green.svg)]()
[![BadBoxes: 0](https://img.shields.io/badge/BadBoxes-0-blue.svg)]()

 * English title: **Adding Bloom filter to the NoSQL Database Redis**
 * Tesi di laurea triennale, Corso di Laurea in Informatica, Università agli
   Studi di Firenze
 * Leggi la [tesi in PDF](https://github.com/rasky/thesis/releases/download/1.0/thesis.pdf)

### Abstract

La tesi presenta una modifica a Redis, un popolare database NoSQL, con la
quale vengono introdotti i filtri di Bloom quale struttura dati aggiuntiva a
quelle già presenti. In particolare, l'aggiunta è utile per arricchire il
sempre crescente numero di strutture dati che Redis offre agli utilizzatori
come strumento di catalogazione dell'informazione.

La tesi è articolata in cinque capitoli: oltre a questa introduzione, nel
secondo capitolo viene descritto il funzionamento e l'architettura di Redis,
descrivendo il contesto scientifico e industriale che ne ha portato alla
nascita, gli scenari applicativi principali in cui viene utilizzato, le
strutture dati che offre, le funzionalità più avanzate e le caratteristiche di
persistenza. Nel terzo capitolo invece vengono descritti i filtri di Bloom,
studiandone gli scenari applicativi, le principali caratteristiche, gli
algoritmi e analizzando nel dettaglio come scegliere i parametri che li
definiscono. Nel quarto capitolo, viene presentato il lavoro svolto di
modifica al codice sorgente di Redis, sottolineando le principali sfide
incontrate e i risultati raggiunti in termini di funzionalità e performance.
Nel quinto ed ultimo capitolo, si commentano i risultati ottenuti e si
descrive una possibile evoluzione del lavoro.

Le modifiche a Redis sono visibile nel [mio fork su
Github](https://github.com/rasky/redis).

### Licenza

Quest'opera è stata rilasciata con licenza Creative Commons Attribuzione - Non
opere derivate 4.0 Internazionale. Per leggere una copia della licenza visita
il sito web http://creativecommons.org/licenses/by-nd/4.0/ o spedisci una
lettera a Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

### Come compilare la tesi

La tesi è stata scritta per `pdflatex`. Una volta installata una distribuzione
LaTeX sul proprio computer, è necessario lanciare `pdflatex` e `biber` in
sequenza più volte, come usuale:

	$ pdflatex thesis.tex
	$ biber thesis.bcf
	$ pdflatex thesis.tex
	$ biber thesis.bcf
	$ pdflatex thesis.tex

A questo punto, sarà stato creato un file `thesis.pdf` corretto. L'ultima
compilazione dovrebbe avvenire con 0 errori, 0 warnings, e 0 bad boxes.

### Altri motori Latex

La tesi può essere compilata correttamente anche con xelatex, ma l'uso di font
leggermente diversi provocherà alcuni piccoli errori tipografici (e molti bad
boxes).

È possibile usare anche [tectonic](https://tectonic.newton.cx) che è un
ambiente di compilazione autocontenuto senza dipendenze.
