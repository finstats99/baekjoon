SELECT  i.animal_id, i.name
  FROM  animal_ins i, animal_outs o
 WHERE  i.animal_id = o.animal_id 
        and i.datetime > o.datetime
 order
    by  i.datetime 