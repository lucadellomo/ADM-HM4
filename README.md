In exercise 1 I extracted json fils and I create a graph G of authors; each link exists if and only if the two authors have at least a common publication and its weight is equal to their Jacard distance.
In exercise 2 I create thow subgraph; the first one is obtained thanks to a "conference_id" given in input and it shows all authors who where there, the second one instead is obtained thanks to an author_id and a "pivot" given in input and it rappresents all nodes that have hop distance at most equal to the "pivot" with the input author_id.
