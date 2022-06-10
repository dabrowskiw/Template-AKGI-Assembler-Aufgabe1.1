# De Novo Assembler - Teil 2

Nachdem Sie in der letzten Übung die notwendigen Grundmethoden und -Klassen erstellt haben, wenden wir uns in dieser Übung dem Aufbau des Graphen zu.

## DBGraph

Die Klasse DBGraph repräsentiert den Graph - also eine Liste an Knoten. Sie soll die folgenden Methoden enthalten:

* Einen leeren Constructor, der die internen Datenstrukturen initialisiert 
* ```add_kmers(self, kmers)```: Fügt die k-mere aus der dictionary ```kmers``` zum Graph hinzu - das ist genau die dictionary, die ```Read.get_kmers()``` zurückgibt. Dabei sollten auch die korrekten Kanten angelegt werden. Wird also ein k-mer zum Graph hinzugefügt, muss überprüft werden, ob k-mere im Graph existieren, von bzw. zu denen Kanten angelegt werden müssen. Sie brauchen dafür dank der Methoden ```get_potential_to``` und ```get_potential_from``` dafür nicht durch alle schon im Graph vorhandenen Knoten zu iterieren - das ist der Grund für den großen Geschwindigkeitsvorteil eines de Bruijn-Graph im Vergleich zum Overlap-Graph. Wichtig ist, dass ein de Bruijn-Graph nur Knoten der gleichen k-mer-Länge enthalten kann. Wird versucht, ein k-mer einer anderen Länge hinzuzufügen, als das erste zum Graphen hinzugefügte k-mer, soll ein ```ValueError``` geworfen werden.
* ```count_edges(self)```: Gibt die Anzahl der Kanten im Graph zurück. Eine Kante sollte immer nur einfach gezählt werden - wenn es zwischen zwei Knoten eine Kante gibt, ist diese ja sowohl im ersten Knoten als Kante zum zweiten, als auch im zweiten Knoten als Kante vom ersten gespeichert. Sie wird aber trotzdem in dieser Methode nur als eine Kante gezählt.
* ```count_nodes(self)```: Gibt die Anzahl der Knoten im Graph zurück.
* ```__str__(self)```: Gibt aus, wie die k-mer-Länge des Graphen ist sowie wie viele Knoten und Kanten der Graph enthält. 

## build_graph

Nun können Sie endlich den Graph aus einer FASTA-Datei erstellen: Implementieren Sie eine top-level-Methode ```build_graph(filename, kmersize)``` die aus den Reads in der FASTA-Datei im Pfad ```filename``` einen Graph mit der k-mer-Länge ```kmersize``` erstellt und zurückgibt.
      
Testen Sie zunächst mit der angehängten Datei test.fasta - Sie sollten bei einer k-mer-Länge von 6 folgendes sehen:

```text
4 k-mere/Knoten
3 Kanten
```

sowie bei einer k-mer-Länge von 2:

```text
8 k-mere/Knoten
17 Kanten
```

Testen Sie dann mit der Datei virus_perfectreads.fasta. Sie sollten bei einer k-mer-Länge von 100 folgendes sehen:

```text
2331 k-mere
2330 Kanten
```

sowie bei einer k-mer-Länge von 10:

```text
2414 k-mere
2460 Kanten
```

Überlegen Sie kurz, was es bedeuten dürfte, wenn die Anzahl der Kanten = Anzahl der k-mere - 1 ist (wie sieht der Graph dann vermutlich aus?). Wird das Rekonstruieren des Genoms einfacher sein, wenn die Anzahl der Kanten über der der k-mere liegt?
