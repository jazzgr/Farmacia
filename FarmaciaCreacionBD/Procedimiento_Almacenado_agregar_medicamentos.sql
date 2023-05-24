create or replace procedure sp_agregar_medicamento(
    v_nom_medicamento varchar2,
    v_formato_medicamento VARCHAR2,
    v_fecha_elav DATE,
    v_fecha_venc DATE,
    v_unidad VARCHAR2,
    v_componente VARCHAR2,
    v_stock NUMBER
    )is

    v_id_medicamento number;
    
begin

    INSERT INTO medicamento(nom_medicamento,formato_medicamento,fecha_elav,fecha_venc,unidad,componente,stock)
    values (v_nom_medicamento,v_formato_medicamento,v_fecha_elav,v_fecha_venc,v_unidad,v_componente,v_stock);
    commit;
end;
    