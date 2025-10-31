[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# September 2025

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/october/images/title.jpeg)

**

This is the SixRackUnits AI hardware newsletter, keeping you up to date with the latest in AI hardware, datacentre technology, and the future of compute. With a field changing this fast, staying on top of everything, or even summarising all the material available can be difficult - so we do it for you.

For a space to share sources and news/updates, join our telegram channel <a href="https://t.me/aihpc_infra_fans">here</a> or if you like short form posts on similar topics, check out the <a href="https://sixrackunits.substack.com/notes">notes</a> section of this newsletter or my <a href="https://www.linkedin.com/in/hitesh-kumar58">LinkedIn</a>.

[**This month's updates:**](#this-months-updates)

- [**Intel announces a prefill GPU - No roadmap yet, but some hope at last**]

---

# This month's updates

## Broadcom TH6 davisson and Thor ultra NIC

## AMD Solar Flare and other stuff

## Nvidia's incredible update pace from OCP25 through to GTC-DC

## Cisco P200

## Intel announces a prefill GPU - No roadmap yet, but some hope at last

As we detailed in our [september issue](https://sixrackunits.substack.com/i/173661634/rubin-cpx-the-gpu-no-one-saw-coming), prefill is the first half of LLM inferencing, and arguably the easier part since it's compute-bound - memory bandwidth being less important. Nvidia took the lead in designing a GPU specifically for prefill aiming at improving performance/$ of CapEx and TCO, and now it seems Intel rather than AMD are the second to announce an ASIC dedicated to this task.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/october/images/crescent_island.jpeg)

*Source: Andreas Schilling on X (@aschilling)*

At OCP25 earlier this month, Intel surprised everyone by formally announcing a [new GPU](https://newsroom.intel.com/artificial-intelligence/intel-to-expand-ai-accelerator-portfolio-with-new-gpu) aimed at the first half of LLM inferencing. Named "Crescent Island" as a product series for now, and likely coming in 2H26, it's expected to compete with Nvidia's Rubin CPX and whatever AMD and other vendors will be releasing at the time. Whatever little we know about it so far sounds quite ordinary however, especially given that it's a year out still.

The prefill GPU is [reported to be air-cooled](https://www.hardwareluxx.de/index.php/news/hardware/grafikkarten/67263-crescent-island-neue-data-center-gpu-auf-basis-von-xe3p-mit-160-gb-lpddr5x-von-intel.html) or at least have an air-cooled variant, and we can safely assume it will come in PCIe form factor, implying that it likely wont exceed a 1000W TDP. We also know that it will provide 160GB of LPDDR5X memory though no details are available yet on the setup of that capacity and the bandwidth we can expect. The choice of using LPDDR5X over GDDR6 or 7 has raised some questions, but when optimising for performance/power and even memory latency, LPDDR5X is the better choice.

We do know about its architecture though, Xe3P hinted at during Intel's tech tour in Arizona prior to OCP and then confirmed in the presentation at the conference. Xe3P continues the lineage of the Xe GPU silicon architectures, serving the Arc-C series of discrete GPUs and focusing on performance per watt according to Intel.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/october/images/crescent_island_xe3p.png)

*Source: Intel*

---

## Other notable headlines

* [Micron starts sampling its 192GB SOCAMM2 LPDDR5X modules, targeting future small-profile AI servers](https://www.tweaktown.com/news/108474/micron-starts-sampling-its-192gb-socamm2-low-power-memory-for-use-in-ai-servers/index.html)
* [Both AMD and Intel to be significant customers of TSMC's upcoming "N2" 2nm process](https://www.tweaktown.com/news/107995/tsmc-2nm-process-expected-to-be-a-game-changer-for-both-amd-and-intel/index.html)
* [Samsung rumoured to supply HBM4 for AMD's MI450X GPUs...](https://www.trendforce.com/news/2025/10/08/news-samsung-reportedly-to-supply-hbm4-for-amd-mi450-in-openai-deal-taking-on-nvidia-sk-hynix/)
*[...And HBM3E for GB300s](https://www.news1.kr/industry/electronics/5934448)
* [Intel showcases "Robinson lake" board architecture for edge/robotics, Pather lake but for rugged deployments](https://x.com/aschilling/status/1976655113419993479)
* [Oracle to deploy a 50,000+ AMD MI450X GPU cluster starting 3Q26](https://www.amd.com/en/newsroom/press-releases/oracle-and-amd-expand-partnership-to-help-customers-ach.html)
* [Meta and Oracle to use SpectrumX Ethernet for their AI clusters](https://www.trendforce.com/news/2025/10/14/news-nvidia-expands-ai-networking-push-as-oracle-and-meta-adopt-spectrum-x-and-ocp-technologies/)
* [Intel to launch a Gaudi 3 + B200 mixed device rack-scale product optimised for LLM inferencing](https://www.linkedin.com/posts/semianalysis_intel-just-took-another-step-on-combining-activity-7385112732125224960-V40q)
* [Synopsys developing LPDDR6 IP on TSMCs N2P process node, hitting up to 86GB/s per module](https://www.tweaktown.com/news/108337/synopsys-teases-silicon-bring-up-of-next-gen-lpddr6-ip-fabbed-on-tsmcs-new-n2p-process-node/index.html)
* [Alibaba cloud claims to reduce its Nvidia GPU use by up to 82% with its new Aegaeon software](https://www.scmp.com/business/article/3329450/alibaba-cloud-claims-slash-nvidia-gpu-use-82-new-pooling-system)
* [Microsoft to use Intel's 18A process for its nex generation of MAIA accelerators](https://www.tweaktown.com/news/108358/microsoft-to-reportedly-use-intel-foundry-and-18a-for-its-next-gen-maia-ai-accelerator/index.html)
* [IBM Spyre AI accelerators now shipping](https://www.nextplatform.com/2025/10/10/ibm-ships-homegrown-spyre-accelerators-embraces-anthropic-for-ai-push/)
* [Samsung to produce NVLink fusion hardware, not just TSMC](https://www.tomshardware.com/samsung-joins-nvidia-nvlink-fusion)
* [Intel foundry reportedly trying to secure AMD as a customer for its 18A and 14A process nodes - for CPUs?](https://www.tweaktown.com/news/108037/intel-is-reportedly-trying-to-secure-amd-as-a-semiconductor-customer-to-make-its-next-gen-chips/index.html)
* [Samsung targeting 3.25TB/s with its HBM4E plans](https://x.com/Jukanlosreve/status/1978268999512445277)
* [Intel announced annual AI hardware release cadence after years of delay and a collapse of its AI roadmap](https://wccftech.com/intel-to-finally-switch-to-an-annual-ai-product-cadence-after-years-of-delay/)

---

[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)
