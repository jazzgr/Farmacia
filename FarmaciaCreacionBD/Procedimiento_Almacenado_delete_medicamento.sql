create or replace procedure sp_delete_medicamento(
    v_id_medicamento number
    )is

begin
    delete medicamento where id_medicamento = v_id_medicamento;
    commit;
 
end;
    