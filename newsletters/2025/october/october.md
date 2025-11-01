[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# September 2025

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/october/images/title.png)

*What defines a network? Is it the sum of the parts connected, or the connections between the individual parts? What would be scarier if broken?*

This is the SixRackUnits AI hardware newsletter, keeping you up to date with the latest in AI hardware, datacentre technology, and the future of compute. With a field changing this fast, staying on top of everything, or even summarising all the material available can be difficult - so we do it for you.

For a space to share sources and news/updates, join our telegram channel <a href="https://t.me/aihpc_infra_fans">here</a> or if you like short form posts on similar topics, check out the <a href="https://sixrackunits.substack.com/notes">notes</a> section of this newsletter or my <a href="https://www.linkedin.com/in/hitesh-kumar58">LinkedIn</a>.

[**This month's updates:**](#this-months-updates)

- [**Broadcom's relentless pace - CPO TH6, and an 800G NIC**]
- [**Nvidia news: OCP25 through to GTC-DC**]
- [**Cisco announces the P200 - a new 100 Terabit switch ASIC**]
- [**Intel announces a prefill GPU - No roadmap yet, but some hope at last**]
- [**Other notable headlines**]

---

# This month's updates

## Broadcom's relentless pace - CPO TH6, and an 800G NIC

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/october/images/broadcom_th6.png)

*Source: Broadcom*

Broadcom has been outpacing its competitors consistently enough now to be widely recognised as the clear leader in (non-nvidia) Ethernet datacentre networking hardware. At OCP25 this month they sustained that momentum by announcing two new major products: a Co-Packaged Optics (CPO) version of the [Tomahawk 6 (TH6) named "Davisson"](https://www.broadcom.com/company/news/product-releases/63626), and a new 800G NIC called the ["Thor Ultra"](https://www.broadcom.com/company/news/product-releases/63641).

The original TH6 was the first major release on our radar, revealed as far back as [June](https://sixrackunits.substack.com/p/june-2025). Since then, Broadcom have shown an incredible pace of development, adding the scale-up focused [Tomahawk Ultra 51.2T](https://sixrackunits.substack.com/i/169948586/broadcoms-inevitable-yet-surprising-new-chip-tomahawk-ultra) and the network-layer defining [Jericho4 51.2T](https://sixrackunits.substack.com/i/172426860/yet-another-switch-from-broadcom-scaling-across-with-jericho) "scale-across" ASICs to their lineup.

The TH6 Davisson now pushes the series forward in energy efficiency, claiming a 3.5x decrease in energy use compared to an equivalent switch (with the original TH6, we should assume) using pluggable optics. The lack of pluggable optics (optical transceivers) avoids the need for many discrete optical modules for converting signals between electrical and optical domains. CPO technology allows for these conversions from incoming signals to happen near the ASIC package and be consolidated to fewer digital signal processors (DSPs), improving signal integrity and reducing power use.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/october/images/broadcom_switch.png)

*Source: Broadcom*

Joining Nvidia's ConnectX-8 and AMD's Vulcano, The Thor Ultra is the third prominent member of the 800G NIC club. Broadcom will likely ship ultra-ethernet consortium (UEC) compliant hardware long before AMD, with the Thor Ultra already implementing various technologies in hardware such as packet-level multipathing, OOO delivery to device memory, and selective re-transmission to name a few. Unlike with the BF4 mentioned later in this issue, this NIC will be used for both frontend and backend networks, likely seeing serious adoption in non-Nvidia deployments.

The NIC will support a PCIe 6 x16 host connection, come with a choice of either 100G or 200G serdes for port-breakout flexibility, and come in PCIe or OCP 3.0 form factors with OSFP ports. Sampling is already underway, and shipping will likely commence sometime in 1H26.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/october/images/broadcom_nic.png)

*Source: Broadcom*

## Nvidia news: OCP25 through to GTC-DC

Across the two major conferences this month, Nvidia has delivered three major announcements to the market:

- A new 800VDC power architecture for the datacentres of the near future
- A long awaited BlueField 4 SuperNIC, and an updated roadmap for the series
- The reveal of the Vera-Rubin superchip and the cable-less VR200 compute tray

### 800VDC

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/october/images/nvidia_800vdc.webp)

*Source: Nvidia*

Arguably one of the most impactful developments in the industry this month (or even year), Nvidia contributed their 800VDC power architecture for datacentres to OCP, making it open to use by all. For datacentre providers and hyperscalers, adopting these higher voltage designs wont just improve the power efficiency of their sites, but will enable them to host the increasingly dense GPU racks Nvidia is planning for the coming years.

Datacentre power delivery architectures determine how power reaches the hardware from the grid. They define how the 13.8kW AC (North America) from the supply is transformed to the 12VDC required by the servers. 800VDC is a significant upgrade from the existing 48/54VDC deployed in many newer Hyperscaler and high end sites, and a complete overhaul compared to 480VAC architectures in older datacentres.

Hosting H100/H200 servers in 480VAC sites already results in a lot of wastage from all the steps and components required, resulting in as little as 75% of the wattage supplied being available for the servers themselves. 54VDC lets newer builds skip some steps and enables deploying the most demanding racks like the GB200 NVL72, but as soon as 2026 when Vera-Rubin racks ship, will still result in poor efficiencies and additional costs for heavy copper busbars and large numbers of PSUs to support the power draw.

For more information on the 800VDC architecture, you can read our article on [XPU.pub](https://xpu.pub/2025/10/28/nvidia-800-v/), where we dive deeper into power architectures and 800VDC.

### BF4 DPU/SuperNIC

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/october/images/nvidia_bf4.jpeg)

*Source: ServeTheHome*

Finally, a full year after it was supposed to be released, the [BlueField 4 SuperNIC](https://blogs.nvidia.com/blog/bluefield-4-ai-factory/) (and DPU?) has been announced for 2026, in sync with the Vera-Rubin product timeline. Ethernet for the front-end and storage networks has been relatively slow in scaling from 400G to 800G, and much of it is just a lack of necessity. Even converged networks handling internet, in-band management, and storage traffic rarely are bottlenecked by the 200G/400G fabrics they're run over.

Dual-port 800G frontend NICs would offer some benefit over existing 400G if used today, though it's not difficult to assume that high-performance storage or other communications offloaded to the frontend network will eventually require more bandwidth. Currently, such cards could provide 4x200G or even 8x100G uplinks with splitter cables, expanding the possibilities of the topologies possible in these deployments.

Anyway, here's what we know so far about the BF4:

Official:

- 800G NIC expressed as two 400G ports
- 64-core Grace CPU on board
- A ConnectX-9 ASIC powering the network interface
- Supporting SpectrumX (Ethernet)

Assumed ([1](https://www.servethehome.com/nvidia-bluefield-4-with-64-arm-cores-and-800g-networking-announced-for-2026/)):

- PCIe gen 6 capable (256GBps BIDI)
- Supporting down to 100G per port configurations
- QSFP112 form factor for the ports

### VR Superchip and tray

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/october/images/nvidia_vr.png)

*Source: Tweaktown*

A stunningly beautiful board was [showcased at GTC-DC](https://www.tweaktown.com/news/108533/nvidia-shows-off-its-next-gen-vera-rubin-superchip-at-gtc-washington-with-two-huge-gpus/index.html?utm_source=newsletter&utm_campaign=newsletter), along with the compute tray that it will sit in. Jensen emphasised the cable-less design now further optimised for lower error rates and better thermal management for the inter-chip communications, though those keeping up with the news would have seen this coming from [SemiAnalysis'](https://newsletter.semianalysis.com/p/another-giant-leap-the-rubin-cpx-specialized-accelerator-rack) (and [our own](https://sixrackunits.substack.com/i/173661634/rubin-cpx-the-gpu-no-one-saw-coming)) post over a month and half ago.

Analysts all over the world have been speculating on what they can infer from the video feed we have so far, and some interesting details have come to light. As we at SixRackUnits noticed almost instantly, the VR superchip will finally have SOCAMM modules on board for its LPDDR (we assume), a welcome surprise given how their involvement in GB300 boards was [delayed](https://www.tomshardware.com/pc-components/gpus/nvidia-postpones-socamm-technology-originally-planned-for-blackwell-ultra-gb300-now-scheduled-for-rubin-rubin-ultra) earlier this year. WeChat user Brendan006 on [Brendan's Packaging Hut](https://mp.weixin.qq.com/s?chksm=c1375a0ef640d3185bbe9bd561c57c931bf860dc456f2a23458c90d7be4e4d4f70de3f03f77f&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1761763695_1&req_id=1761763695454495&mid=2247484034&sn=5a3f205c723e6c3fd584fec7caadd9ab&idx=1&__biz=MzkwOTc0MjU2Mw%3D%3D&scene=169&subscene=200&sessionid=1761763694) also took a close look at the Vera CPU die and noticed that it's likely 6 separate dies on an interposer as opposed to a monolithic design.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/october/images/nvidia_vr_zoomed.png)

## Cisco's P200 - a new 100 Terabit switch ASIC

## Intel announces a prefill GPU - No roadmap yet, but some hope at last

As we detailed in our [september issue](https://sixrackunits.substack.com/i/173661634/rubin-cpx-the-gpu-no-one-saw-coming), prefill is the first half of LLM inferencing, and arguably the easier part since it's compute-bound - memory bandwidth being less important. Nvidia took the lead in designing a GPU specifically for prefill aiming at improving performance/$ of CapEx and TCO, and now it seems Intel rather than AMD are the second to announce an ASIC dedicated to this task.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/october/images/crescent_island.jpeg)

*Source: Andreas Schilling on X (@aschilling)*

At OCP25 earlier this month, Intel surprised everyone by formally announcing a new prefill-focused [new GPU](https://newsroom.intel.com/artificial-intelligence/intel-to-expand-ai-accelerator-portfolio-with-new-gpu), after scrapping their Gaudi and Falcon shores roadmap's and the many months of silence since. Now, this new series named "Crescent Island", scheduled for release in 2H26, is expected to compete with Nvidia's Rubin CPX and whatever AMD and other vendors will be releasing at the time.

The GPU is [reported to be air-cooled](https://www.hardwareluxx.de/index.php/news/hardware/grafikkarten/67263-crescent-island-neue-data-center-gpu-auf-basis-von-xe3p-mit-160-gb-lpddr5x-von-intel.html) or at least have an air-cooled variant, and we can safely assume it will come in PCIe form factor, implying that it likely wont exceed a 1000W TDP. We also know that it will provide 160GB of LPDDR5X memory though no details are available yet on the setup of that capacity and the bandwidth we can expect. The choice of using LPDDR5X over GDDR6 or 7 has raised some questions, but when optimising for performance/power and even memory latency, LPDDR5X is the better choice.

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
