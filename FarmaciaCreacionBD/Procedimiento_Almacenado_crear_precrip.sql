create or replace procedure sp_crear_prescrip(
    v_id_medicamento number,
    v_id_paciente number,
    v_restar_stock NUMBER
    )is

    v_operacion_stock number;
    v_stock_total number;
    v_fecha_actual date;
    
begin

    select stock
    
        into v_operacion_stock
    
    from medicamento
    where id_medicamento = v_id_medicamento;


    v_stock_total:= (v_operacion_stock - v_restar_stock );  
    
    UPDATE medicamento set stock = v_stock_total where id_medicamento = v_id_medicamento;


    SELECT CURRENT_DATE 
    
        into v_fecha_actual
    
    FROM DUAL;

    INSERT into prescripcion (fecha_emision,cantidad,id_medicamento,id_paciente) VALUES (v_fecha_actual, v_restar_stock, v_id_medicamento,v_id_paciente);
    commit;
end;