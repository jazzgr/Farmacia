create or replace procedure sp_obtener_stock(
    v_id_medicamento number,
    v_stock out number
    )is
begin

select stock

into v_stock

from medicamento
where id_medicamento = v_id_medicamento;

end;
    