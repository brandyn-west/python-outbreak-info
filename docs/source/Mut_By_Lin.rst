mutations_by_lineage(mutation, location, pango_lin)
---------------------------------------------------
.. note:: Endpoint: https://api.outbreak.info/genomics/mutations-by-lineage

.. autofunction:: outbreak_data.mutations_by_lineage

.. code-block:: 
   :caption: **Example:** Get prevalence of S:E484K across all lineages in the U.S. Endpoint: https://api.outbreak.info/genomics/mutations-by-lineage?mutations=S:E484K&location_id=USA

   df = mutations_by_lineage('s:e484k', 'USA')
