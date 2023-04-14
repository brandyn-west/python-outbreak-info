lineage_mutations(pango_lin, mutation, freq)
--------------------------------------------

.. autofunction:: outbreak_data.lineage_mutations
 
.. code-block::
   :caption: Basic query:
   
        Ex:  foo = lineage_mutations('b.1.1.7')

.. code-block::
   :caption: Mutiple queries for lineages and mutations can be separated by ","

        Ex:  foo = lineage_mutations('b.1.1.7, b.2, ay.2')

.. code-block::
   :caption: Use 'OR' in a string to return overlapping mutations in multiple lineages.

        Ex:  foo = lineage_mutations('ba.2 OR b.1.1.7')

..code-block::
  :caption: **Example:** Get all mutations in A.27 lineage. https://api.outbreak.info/genomics/lineage-mutations?pangolin_lineage=A.27
  
   df = lineage_mutations('a.27') 
