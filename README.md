# De Novo Assembler - Teil 1

In dieser Aufgabe beginnen Sie, einen eigenen de novo-Assembler zu entwickeln, der aus NGS-Daten ein Genom rekonstruieren kann. Zunächst arbeiten Sie mit beispielhaften, fehlerfreien Daten, später kommen Fehlerkorrektur in den Reads sowie im Graph dazu.

In diesem ersten Teil sollen Sie die Grundlage für die Erstellung eines de Bruijn-Graphen aus Reads legen. Zu diesem Zweck stehen Ihnen zwei FASTA-Dateien mit Readsequenzen zur Verfügung ("data/test.fasta" sowie "data/virus_perfectreads. fasta"). 

Für die Verarbeitung der Daten müssen Sie einige Klassen und Top-Level-Methoden implementieren.

## Read

Die Klasse ```Read``` repräsentiert einen einzelnen Sequenzier-Read. Da Reads aus FASTA-Dateien gelesen werden, soll die Klasse auch in der Lage sein, die Sequenzinformation aus entsprechend formatierten Zeilen zu extrahieren. Eine FASTA-Datei ist wie folgt aufgebaut:

```text
>Readname 1
Sequenzzeile 1
Sequenzzeile 2
.
.
Sequenzzeile n
>Readname 2
Sequenzzeile 1
Sequenzzeile 2
.
.
Sequenzzeile n
.
.
.
>Readname n
Sequenzzeile 1
Sequenzzeile 2
.
.
Sequenzzeile n
```

Die FASTA-Datei enthält also beliebig viele Reads, wobei jeder Read mit einem Readnamen anfängt, der daran zu erkennen ist, dass die Zeile mit einem ```>``` beginnt. Danach folgt mindestens eine Zeile mit Basen (A, G, T oder C). Falls mehrere Zeilen mit Basen vorhanden sind, beschreiben diese zusammen die gesamte Sequenz, müssen also miteinander verkettet werden.

Implementieren Sie in der Klasse ```Read``` die folgenden Methoden: 

* Einen Constructor, der als String-Array die ihn beschreibenden Zeilen aus einer FASTA-Datei bekommt 
* ```get_kmers(self, kmersize)```: Gibt alle k-mere der Länge k des Reads als dictionary zurück. Key soll dabei die Sequenz des k-mers sein, value die Häufigkeit (also wie viel Mal dieses k-mer in der Read-Sequenz vorkommt)
* ```__str__(self)```: Gibt den Read als String aus, in der Form "Name: Sequenz", wobei bei Sequenzen mit einer Länge von mehr als 20 Basen nur die ersten 20 Basen, gefolgt von "..." ausgegeben werden sollen. Beispiel: "Read 2: AGTCGTAGCGTACCGTAGCC..." 
* ```__repr__(self)```: Gibt die in ```__str__``` definierte String-Repräsentation zurück (für eine einfachere Ausgabe auf der Kommandozeile)    
* ```__eq__(self, other)```: Der Vergleichsoperator, der aufgerufen wird, wenn zwei Objekte mit ```==``` miteinander verglichen werden. Soll ```true``` zurückgeben, falls Name und Sequenz des Reads ```other``` mit diesem Read identisch sind, sonst false (auch, wenn ```other``` gar kein ```Read``` ist - nutzen Sie dafür die Methode ```isinstance```)

## read_fasta

Das Einlesen der gesamten FASTA-Datei soll in der top-level-Methode ```read_fasta(filename)``` erfolgen, die als ```filename``` den Pfad zu einer FASTA-Datei bekommt und eine Liste von ```Read```-Objekten zurückgibt, die die einzelnen Reads aus der FASTA-Datei enthalten.

## DBGNode

Die Klasse DBGNode soll einen Knoten im De Bruijn-Graph repräsentieren - also ein k-mer mit einer Liste von ein- und ausgehenden Kanten. Implementieren Sie dafür die folgenden Methoden:

* Einen Constructor, der die Sequenz des Knotens bekommt (also seine k-mer-Sequenz)
* ```get_potential_from(self)```: Gibt als Liste alle k-mer-Sequenzen zurück, von denen es theoretisch eine Kante zu diesem Knoten geben könnte. Bedenken Sie, was die Definition eines De Bruijn-Graphen ist: Wenn wir das Alphabet ```["A", "G", "T", "C"]``` nutzen, können diese potentiellen Knoten sehr einfach aufgelistet werden!
* ```get_potential_to(self)```: Gibt, ähnlich ```get_potential_from(self)```, die Liste aller k-mer-Sequenzen zurück, zu denen von diesem Knoten aus eine Kante gehen könnte.
* ```add_edge_to(self, eto)```: Fügt zu der internen Kantenliste eine Kante zu der ```DBGNode``` ```eto``` hinzu. Falls diese Kante schon existiert, wird stattdessen ihr Gewicht um 1 erhöht.
* ```add_edge_from(self, efrom)```: Fügt zu der internen Kantenliste eine Kante von der ```DBGNode``` ```efrom``` hinzu. Falls diese Kante schon existiert, wird stattdessen ihr Gewicht um 1 erhöht.
* ```get_edge_from_weight(self, other)```: Gibt das Gewicht der Kante von der ```DBGNode``` ```other``` zu diesem Knoten zurück (0, falls keine solche Kante existiert).
* ```get_edge_to_weight(self, other)```: Gibt das Gewicht der Kante von diesem Knoten zur ```DBGNode``` ```other``` zurück (0, falls keine solche Kante existiert).
