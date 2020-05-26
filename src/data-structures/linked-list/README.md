# Lista encadeada

Na área de ciência da computação, uma lista ligada (ou lista simplesmente encadeada) é uma vantajosa alternativa na implantação de arrays. Arrays implica que o tamanho de N elementos devem ser fixados a priori.

Uma alternativa para esta desvantagem é o uso de lista encadeadas, que permite a criação de arrays sem um número de N elementos fixo.

Uma lista é formada por nós. Nó é um objeto composto que armazena uma referência para um elemento ou objeto qualquer e uma referência next (próximo) que permite fazer a ligação com o próximo nó da lista até que o último aponte para uma região de memória nula (null).

O primeiro e o último nós de uma lista são chamados respectivamente de cabeça (referência head) e cauda (referência tail) da lista.

![](https://upload.wikimedia.org/wikipedia/commons/9/9c/Single_linked_list.png?1590507080876)

## Métodos implementados

### **Construtor**
 Cria uma lista encadeada e cria um nó 'Cabeça' sem dados e como próximo nó o valor 'None', este método é invocado automaticamente quando feito o instanciamento.
 
 **Caso de uso:**
 
 ```
 import linkedlist
 
 my_list = linkedlist.LinkedList()
 ```
### Destrutor
 Altera a propriedade 'próximo nó' do 'Cabeça' para o valor 'None', assim, desencadeando toda a sequência montada, desfazendo a lista.
 
  **Caso de uso:**
 
 ```
 import linkedlist
 
 my_list = linkedlist.LinkedList()
 
 del my_list()
 ```
### append
Adiciona um novo nó com o dado desejado, no **final** da lista encadeada, alem de fazer o apontamento do penultimo nó para ele e apontamento dele para o próximo igual a 'None'.

**Caso de uso:**

```
 import linkedlist
 
 my_list = linkedlist.LinkedList()
 
 mylist.append(valor_dentro_do_novo_no)
 ```
### prepend
Adiciona um novo nó com o dado desejado, no **inicio** da lista encadeada, alem de fazer o apontamento da 'Cabeça' para ele e apontamento dele para o antigo primeiro nó.

**Caso de uso:**

```
 import linkedlist
 
 my_list = linkedlist.LinkedList()
 
 mylist.prepend(valor_dentro_do_novo_no)
 ```
### erase
Dado um index, ira percorrer a lista encadeada começando no nó 'Cabeça', chegando ao nó com index desejado, ele faz o apontado do nó anterior para o proximo nó, desencadeando este nó da lista. 

**Caso de uso:**

```
 import linkedlist
 
 my_list = linkedlist.LinkedList()
 
 mylist.prepend(valor_dentro_do_novo_no)
 mylist.erase(0) #sendo 0 o index, primeira posicao
 ```

### length
Função que devolve a quantidade de nós na lista, sem contar o nó 'Cabeça'.
**Caso de uso:**

```
 import linkedlist
 
 my_list = linkedlist.LinkedList()
 
 print my_list.length()
```

### get
Função que percorre a lista encadeada começando no nó 'Cabeça' até o index desejado, retornando uma cópia do valor armazenado dentro do objeto.

**Caso de uso:**

```
 import linkedlist
 
 my_list = linkedlist.LinkedList()
 
 mylist.prepend(valor_dentro_do_novo_no)
 
 print my_list.get(0) #sendo 0 o valor do index
```

### display
Faz uma cópia dos dados armazenados dentro dos objetos da lista encadeada em um arranjo, na mesma ordem e imprime.

**Caso de uso:**
```
 import linkedlist
 
 my_list = linkedlist.LinkedList()
 
 mylist.prepend(valor_dentro_do_novo_no)
 
 my_list.display()
```

## Referências 
* [YouTube](https://www.youtube.com/watch?v=njTh_OwMljA&index=2&t=1s&list=PLLXdhg_r2hKA7DPDsunoDZ-Z769jWn4R8)
* [WikiPedia](https://pt.wikipedia.org/wiki/Lista_simplesmente_ligada)


*Casos de uso retratados na linguagem Python*
