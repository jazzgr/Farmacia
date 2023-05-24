create or replace procedure sp_update_stock(
    v_id_medicamento number,
    v_stock NUMBER
    )is
    
    v_suma_stock number;
    v_stock_total number;
begin

select stock

into v_suma_stock

from medicamento
where id_medicamento = v_id_medicamento;

    v_stock_total:= (v_stock + v_suma_stock);

    UPDATE medicamento set stock = v_stock_total where id_medicamento = v_id_medicamento;
    commit;

end;
    