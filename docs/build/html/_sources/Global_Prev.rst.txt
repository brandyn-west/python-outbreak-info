global_prevalence(pango_lin, mutations, cumulative)
----------------------------------------------------
.. attention:: This function is deprecated. Consider using the daily_prev() function instead.
.. autofunction:: outbreak_data.global_prevalence

.. code-block:: 
   :caption: **Examples:** Global daily prevalence of B.1.1.7 lineage. https://api.outbreak.info/genomics/global-prevalence?pangolin_lineage=b.1.1.7

   df = global_prevalence('b.1.1.7')

.. code-block::
   :caption: Global daily prevalence of B.1.1.7 lineage with S:E484K mutation. https://api.outbreak.info/genomics/global-prevalence?pangolin_lineage=b.1.1.7&mutations=S:E484K

   df = global_prevalence('b.1.1.7', 's:e484k')

.. code-block::
   :caption: Cumulative global prevalence of B.1.1.7. https://api.outbreak.info/genomics/global-prevalence?pangolin_lineage=b.1.1.7&cumulative=true

   df = global_prevalence('b.1.1.7', cumulative = True)
