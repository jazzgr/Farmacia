create or replace procedure sp_update_stock(
    v_id_medicamento number,
    v_stock NUMBER
    )is

begin
    UPDATE medicamento set stock = v_stock where id_medicamento = v_id_medicamento;
    commit;

end;
    