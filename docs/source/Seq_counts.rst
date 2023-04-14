sequence_counts(location, cumulative, sub_admin)
-------------------------------------------------
.. note:: Endpoint: https://api.outbreak.info/genomics/sequence-count

.. autofunction:: outbreak_data.sequence_counts

.. code-block::
   :caption: **Examples:** Number of sequences per day globally. Endpoint: https://api.outbreak.info/genomics/sequence-count

    df = sequnce_counts()

.. code-block::
   :caption: Cumulative number of sequences for every US state. Endpoint:  https://api.outbreak.info/genomics/sequence-count?location_id=USA&cumulative=true&subadmin=true

    df = sequence_counts('USA', True, True)

.. code-block::
   :caption: Daily number of sequences for California. Endpoint:  https://api.outbreak.info/genomics/sequence-count?location_id=USA_US-CA

    df = sequence_counts('USA_US-CA')


