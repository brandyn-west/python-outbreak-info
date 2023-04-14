prevalence_by_location(location, ndays, nday_threshold, other_threshold, other_exclude, cumulative, startswith, server, auth):
------------------------------------------------------------------------------------------------------------------------------
.. note:: Endpoint: https://api.outbreak.info/genomics/prevalence-by-location-all-lineages
 
.. autofunction:: outbreak_data.prevalence_by_location


.. code-block::
   :caption: **Example:** Give prevalence of all lineages in the U.S., classify lineages that are below 0.03 prevalence for at least 5 days over the last 60 days as "Other", and exclude p.1 from "Other" even if conditions for "Other" are satisfied.  Endpoint: https://api.outbreak.info/genomics/prevalence-by-location-all-lineages?location_id=USA&other_threshold=0.03&nday_threshold=5&ndays=60

   df = prevalence_by_location('USA', 60, 5, 0.03, 'p.1')        

