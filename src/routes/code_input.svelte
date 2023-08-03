
<script lang = ts  src="https://cdn.jsdelivr.net/pyodide/v0.20.0/full/pyodide.js">

    // code input
    //import CodeMirror from "svelte-codemirror-editor";
    import CodeMirror, { basicSetup } from './CodeMirror.svelte'
    import { EditorState, Compartment} from "@codemirror/state"
    import { sql } from "@codemirror/lang-sql";
    import { basicDark } from 'cm6-theme-basic-dark'

    //styling
    import Button, { Label } from '@smui/button';
    import Select, { Option } from '@smui/select';
    import CircularProgress from '@smui/circular-progress';
    import Tooltip, { Wrapper } from '@smui/tooltip';
    import Fab from '@smui/fab';
    import { Icon } from '@smui/common';

    import Modal from './Modal.svelte';


    //import convert_sql from './converter.js';
    import { get } from 'svelte/store';
    import { pyodide_status, pyodide_load } from './stores.js';

    // for holding input
    let docStore;

    // for updating output
    let store_output;
    let store_output_status = false;

    let display_div = "display: none;";

    let default_sql = `SELECT * FROM TABLE1 \n\n\n\n\n\n\n\n\n\n\n\n`

    let showModal = false;

    function changeHandler({detail: {tr}}) {
        console.log('change', tr.changes.toJSON())
    }



    //set default extensions for theme and language:
    let language = new Compartment

    let extensions = [
            basicSetup,
            language.of(sql()),
            basicDark
        ]



    // function update_output(store) {
    //     console.log(store)

    //     console.log('clicked update')
    //     store_output_status = true
    //     console.log(store_output_status)

    //     store_output.set("test")

    //     //store_output.set(convert_sql(store))
    // }


    let pyodide;
    let pyodide_loaded = false;
    let display_loading = false;

    async function convert_sql(sql_input, input_dialect, target_dialect) {
        display_loading = true;

        console.log('clicked update')
        console.log("input query:  ", sql_input)
        console.log("input dialect:  ", input_dialect)
        console.log("output dialect:  ", target_dialect)

        console.log("pyodide loaded", pyodide_loaded)
        pyodide_loaded = get(pyodide_status)

        if (pyodide_loaded === false) {
            console.log("refreshing pyodide")
            pyodide = await loadPyodide();
            pyodide_status.set(true);
            console.log("loaded pyodide");
            pyodide_load.set(pyodide);
        }

        pyodide = get(pyodide_load)

        await pyodide.toPy(sql_input)
        let sql_namespace = {sql_text: sql_input,
                            read_dialect: input_dialect,
                            write_dialect: target_dialect};

        console.log("namespace for pyodide: ", sql_namespace)
        pyodide.registerJsModule("sql_namespace", sql_namespace);



        await pyodide.loadPackage('micropip')


        //const py_sql_convert_path = await fetch("/src/routes/sql_convert/sql_convert.py")
        const py_sql_convert_path = await fetch("sql_convert.py")
        const py_script_text = await py_sql_convert_path.text()

        // console.log(script_text)

        await pyodide.runPythonAsync(py_script_text)


        console.log("converted query: ")
        console.log(converted_query)

        console.log(sql_namespace.converted_query)

        store_output.set(sql_namespace.converted_query + `\n\n\n\n\n`)

        display_div = "";
        display_loading = false;

        }


        $: display_div = display_div;
        $: display_loading = display_loading;
        

    let supported_dialects = ['tsql', 'snowflake', 'oracle', 'teradata', 'bigquery', 'databricks', 'sqlite', 'mysql', 'postgres'];
    let input_dialect = 'tsql';
    let target_dialect = 'snowflake';

</script>
 
<Modal bind:showModal>

</Modal>


<!-- just styling stuff here: -->

<div id="codespace" style="display:flex; flex-direction:column;">

    <div style="display:flex; flex-grow:1; flex-direction:column; width:90%; padding: 20px;">

        <div style="display:flex; flex-direction:row; justify-content:space-between;">
            <h3>
                SQL Text Input
            </h3>

            <Wrapper style="padding:20px">
                <Fab on:click={() => (showModal = true)} mini>
                <Icon class="material-icons">help</Icon>
                </Fab>
                <Tooltip>
                    Click to show the glossary of sql dialects
                </Tooltip>
            </Wrapper>

        </div>


        

        <div class="code-mirror-container">
            <CodeMirror doc={default_sql}
                bind:docStore={docStore}
                extensions={extensions}
                on:change={changeHandler}
                >
            </CodeMirror>

        </div>
    </div>



    <div style="padding: 20px">


        <Select bind:value = {input_dialect} label = "Select Input Dialect">
            {#each supported_dialects as dialect}
            <Option value = {dialect}> {dialect} </Option>
            {/each}
        </Select>    
        
        <Select bind:value = {target_dialect} label = "Select Target Dialect">
            {#each supported_dialects as dialect}
            <Option value = {dialect}> {dialect} </Option>
            {/each}
        </Select>  




        <Button on:click={ convert_sql( $docStore, input_dialect, target_dialect ) } variant="raised">
            <Label> Convert </Label>
        </Button>

    </div>

    <div style="padding: 20px">

    </div>
    

    {#if display_loading}
    <div style="display:flex; flex-grow:1; flex-direction:column; width:90%; padding: 20px;">

        <CircularProgress style="height: 32px; width: 32px;" indeterminate />
        <p>
            *first run takes longer, subsequent runs go faster
        </p>
    </div>
    {/if}

    <div style="display:flex; flex-grow:1; flex-direction:column; width:90%; padding: 20px; {display_div}">


        <h3>
            SQL Text Output
        </h3>

        
        <div class="code-mirror-container">
            <!-- <textarea bind:value={$store}></textarea>

            <pre>
                You typed =>{$store}&lt;=
            </pre> -->


            <CodeMirror doc={default_sql}
                bind:docStore={store_output}
                extensions={extensions}
                on:change={changeHandler}
                >
            </CodeMirror>


        </div>
        

    </div>
</div>



<!-- <div>
    <button on:click = {sql_input }>
        convert!
    </button>
</div> -->



<style>

    /* For the CodeMirror editor: */

    :global(.codemirror) {
        border: 1px solid #ddd;
        color: white;

    }

    /* For the returned SQL */

	h3 {
		color: white;
	}

    h2 {
		color: white;
	}

    .code-mirror-container {
        filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
    }

</style>

