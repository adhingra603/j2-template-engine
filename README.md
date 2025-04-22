# j2-template-engine
##### Dockerized Solution :whale:
Renders a set of Jinja templates with a set of YAML dictionaries to the output dir.

## Notes:
- Templates must end with `'.j2'` extension
- YAML dictionaries are loaded lexically and flattened. This behavior provides a powerful way to apply overrides if desired.  Conversely, be aware of this behavior if loading dictionaries containing matching keys.
- Output dir is created idempotically (ex: `mkdir -p </foo/bar/non-existent/output`)

## Usage:
- [render.sh](./render.sh) shell script attaches current dir to container
```
❯ render.sh -d dictionaries -t templates -o myoutputfolder
```
## Parameters:

| argument | default | description |
| -------- | ------- | ----------- |
| '-d', '--dictionaries' | default='./examples/dictionaries' | Folder containing yaml dictionaries |
| '-t', '--templates' | default='./examples/templates' | Folder containing templates to be rendered |
| '-o', '--output' | default='./output' | Folder to write rendered templates |

## Examples:
An [examples](./examples) folder contains dictionaries and templates to experiment with.

### Example session
```
❯ pwd
/tmp/examples

❯ find .
.
./templates
./templates/dns.yaml.j2
./templates/vpc.yaml.j2
./dictionaries
./dictionaries/sandbox.yaml
./dictionaries/global.yaml

❯ ~/workspaces/paas/j2-template-engine/render.sh -d dictionaries -t templates -o fonzie3
❯ find .
.
./fonzie3
./fonzie3/dns.yaml
./fonzie3/vpc.yaml
./templates
./templates/dns.yaml.j2
./templates/vpc.yaml.j2
./dictionaries
./dictionaries/sandbox.yaml
./dictionaries/global.yaml
❯ cat fonzie3/vpc.yaml
module "vpc" {
  source              = git.com/cainc
  vpcname             = k8s1
  domain_name         = sandbox.cainc.internal
  is_spoke            = True
  k8s_nacl            = True
  vpcnum              = 9
  peered_to_hub       = 0
  domain_name_servers: AmazonProvidedDNS
}%

❯ cat templates/vpc.yaml.j2
module "vpc" {
  source              = {{ modules.terraform_module_vpc }}
  vpcname             = {{ vpc.vpcname }}
  domain_name         = {{ vpc.domain_name }}
  is_spoke            = {{ vpc.is_spoke }}
  k8s_nacl            = {{ vpc.k8s_nacl }}
  vpcnum              = {{ vpc.vpcnum }}
  peered_to_hub       = {{ vpc.peered_to_hub }}
  domain_name_servers: {{ domain_name_servers }}
}
```