import { writable } from 'svelte/store';

// export const sql_input = writable("select * from test_store");
//export const store_output_text = writable("select * from test_store");

export const pyodide_load = writable("");
export const pyodide_status = writable(false);
