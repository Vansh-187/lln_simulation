rule all:
    input:
        f"plots/{config['n']}.png"

rule lln_sim:
    input:
        script = "scripts/lln_sim.py"
    params:
        n = config["n"],
        k = lambda wildcards: wildcards.k,
        repeats = config["repeats"]
    output:
        outfile = f"results/{config['n']}/{{k}}.txt"
    shell:
        "python {input.script} --n {params.n} --k {params.k} --repeats {params.repeats} --output {output.outfile}"

rule plot:
    input: 
        txts = expand(f"results/{config['n']}/{{k}}.txt", k=config["k_values"])
    output: 
        plot = f"plots/{config['n']}.png"
    params:
        folder = f"results/{config['n']}"
    shell:
        "python scripts/plot.py --inputfolder {params.folder} --output {output.plot}"