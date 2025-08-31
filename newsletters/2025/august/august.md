[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# August 2025

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/title.jpeg)

*Is a material form a requirement for true intelligence? Does being limited to certain modalities of input result in less capability within those modalities than an intelligence that can handle more modalities of input? If so, will achieving human-level intelligence require AI models to have humanoid robotic bodies?*

This is the SixRackUnits AI hardware newsletter, keeping you up to date with the latest in AI hardware, datacentre technology, and the future of compute. With a field changing this fast, staying on top of everything, or even summarising all the material available can be difficult - so we do it for you.

For a space to share sources and news/updates, join our telegram channel <a href="https://t.me/aihpc_infra_fans">here</a> or if you like short form posts on similar topics, check out the <a href="https://sixrackunits.substack.com/notes">notes</a> section of this newsletter or my <a href="https://www.linkedin.com/in/hitesh-kumar58">LinkedIn</a>.

[**This month's updates:**](#this-months-updates)
  - [**HotChips 25! - everything of note**](#hotchips-25-everything-of-note)
  - [**Yet another switch from Broadcom - scaling across with Jericho4**](#yet-another-switch-from-broadcom-scaling-across-with-jericho4)
  - [**B300 GPU finally detailed**](#b300-gpu-finally-detailed)
  - [**PCIe 8.0 announced**](#pcie-80-in-the-works-and-we-dont-even-have-pcie-60-cpus-yet)
  - [**Other notable headlines**](#other-notable-headlines)

---

# This month's updates

## HotChips 25! - everything of note

HotChips is the annual industry event for high-performance silicon, with both the big and small names showcasing their advancements in the field. This year's event seemed dominated by relatively few players, Nvidia, Meta, and Google stealing much of the spotlight. Between all the announcements and reveals made at the event, there were just too many updates to cover here comprehensively. Instead, we'll present some of the highlights that we think are the most important and interesting.

### Nvidia: Spectrum-X switches and a scale-across fabric

Spectrum-X was originally Nvidia's reaction to Ethernet gaining traction after the market showed strong signs of InfiniBand lock-in fatigue. Now, rivalling InfiniBand in its adoption among Nvidia's largest customers, Spectrum-X is innovating in two key areas: massive 512-port 400T switches, and expanding beyond the confines of a datacentre.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/hotchips_nvidia_switches.png)

*Source: Nvidia*

On the first item, a lot was already revealed back in GTC25 in March, see [our article](https://sixrackunits.substack.com/i/160297922/nvidia-and-partners-announce-next-gen-datacentre-switches-with-co-packaged-optics) from back then detailing almost exactly the same information. The only [new content](https://www.tweaktown.com/news/107372/nvidias-new-spectrum-x-ethernet-silicon-photonics-enters-the-chat-a-game-changer-for-ai/index.html) is some more detail on the observed (we assume) performance (according to Nvidia) of the 102T switch, and pictures of the switch that uses optical transceivers rather than the CPO version that was shown back then.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/hotchips_nvidia_spectrumxgs.png)

*Source: Nvidia*

The other major reveal was the [Spectrum-XGS](https://nvidianews.nvidia.com/news/nvidia-introduces-spectrum-xgs-ethernet-to-connect-distributed-data-centers-into-giga-scale-ai-super-factories) add-on to Nvidia's ethernet fabric technology, a "scale-across" stack designed to connect multiple scale-out domains (datacentres) together. More on the meaning of scale-across in our article later in this post. Spectrum-XGS claims to expand telemetry, congestion control, and load-balancing all indefinitely with respect to the number of devices, and should be a lot better at reducing cross-datacentre latency where connections can be an order of magnitude or two longer than those within a datacentre.

### Google: Ironwood TPUv7 and TPU racks

We shared everything that was available on the TPUv7 back in [April](https://sixrackunits.substack.com/i/162620183/ironwood-googles-seventh-gen-tpu) when it was announced, and a lot of this remain unchanged. We made a mistake in thinking it would be six stacks of 12hi HBM3E, and we now see it'll be eight stacks instead. Memory capacity and bandwidth remain unchanged thankfully. The compute capacity is interesting though, since at 4.5 PFLOPs of FP8, the TPUv7 brings the same amount of inference performance as the B200/300 and the MI350X. It seems the TDP hasn't yet been confirmed but anything below 1kW would be surprising.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/hotchips_google_tpuv7.webp)

*Source: Google*

But Google's session was still very revealing, as they showed much more on how the Ironwood scales to the server and rack level. We saw earlier that they were aiming for 4 chips per board, but now its been confirmed in their slides. They're sticking to PCIe 5.0 for the H2D, which is unsurprising given that TPUs rely entirely on their mesh scale-up for D2D. For this purpose, they'll have an incredible 18 OSFP (800G) ports per board, so many ports actually, that they couldn't even fit all 18 on one side of the board and instead had to put 2 underneath on the other side.  

It was also really interesting to hear them talk about the per-chip variable flow rates for the liquid cooling step. Having a constant and equal flow rate was just assumed to be the sensible idea, but different chips on the same board could be doing very different things in theory, and hence will need different coolant flow rates.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/hotchips_google_tpu_server.webp)

*Source: Google*

We knew they'd be aiming for clusters (or "pods") of up to 9216 devices in a single ICI (Inter-Chip-Interconnect) domain and [predicted two topologies](https://sixrackunits.substack.com/i/162620183/ironwood-googles-seventh-gen-tpu): a 96x96 2D torus, or a 32x32x9 3D torus. But now we see exactly how they'll implement this - a 64 x 16 x 9 3D torus. This makes sense, as their chosen rack design still fits 64 of these huge TPUs in 16 trays of 4 chips (one board) perfectly well. This lets them keep the pod of 64 connected by copper and lets them use their [OCS](https://www.datacenterdynamics.com/en/analysis/mission-apollo-behind-googles-optical-circuit-switching-revolution-mag/) (Optical Circuit Switching) technology to extend ICI to 144 racks in the superpod.  

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/hotchips_google_tpu_rack.webp)

*Source: Google*

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/hotchips_google_tpu_ici.png)

*Source: Google*

### AMD: Scale-up fabrics and the MI350X

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/hotchips_amd_mi350.png)

*Source: AMD*

AMD detailed the their two upcoming Instinct series GPUs, the MI350X and the MI355X. As we detailed back in [June](https://sixrackunits.substack.com/i/167217145/amd-delivers-a-roadmap-to-defeat-nvidia), the two are almost identical in their memory and compute system designs. The only real difference of relevance to customers will be the TDP: the 350 at 1kW and the 355 at 1.4kW. The first is aimed at 8-GPU air cooled servers where datacentres prefer to stick to ~10kW per 6-8U of rack space, and the second is aimed at 4 or 8-GPU liquid cooled servers, where the power can reach 15 or even 18kW per 4-6U of space. For more info on the rack-scale setups and topologies, see Semianalysis' excellent [article](https://semianalysis.com/2025/06/13/amd-advancing-ai-mi350x-and-mi400-ualoe72-mi500-ual256/).

Oracle has already announced an [order of over 130K MI355X GPUs](https://www.datacenterdynamics.com/en/news/oracle-to-deploy-cluster-of-more-than-130000-amd-mi355x-gpus/) for their upcoming zettascale AMD cluster, and other Hyperscalers and the AMD-centric neoclouds will no doubt be placing smaller orders. We could very well be seeing AMD taking a double digit market share from Nvidia soon if their [software can improve](https://semianalysis.com/2025/06/13/amd-advancing-ai-mi350x-and-mi400-ualoe72-mi500-ual256/#rocm-software-improvements) fast enough to avoid the issues that prevented the rise of MI250X and MI300X GPUs.

To compare to the Blackwell series ([1](https://resources.nvidia.com/en-us-dgx-systems/dgx-b200-datasheet) [2](https://resources.nvidia.com/en-us-dgx-systems/dgx-b300-datasheet?ncid=no-ncid) [3](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/product-briefs/amd-instinct-mi350x-gpu-brochure.pdf) [4](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/product-briefs/amd-instinct-mi355x-gpu-brochure.pdf)):

| Feature                | AMD MI350X      | AMD MI355X      | NVIDIA B200         | NVIDIA B300         |
|------------------------|-----------------|-----------------|---------------------|---------------------|
| Memory Capacity        | 288 GB HBM3e    | 288 GB HBM3e    | 180 GB HBM3e        | 288 GB HBM3e        |
| Memory Bandwidth       | 8 TB/s          | 8 TB/s          | 8 TB/s              | 8 TB/s              |
| Form Factor            | OAM             | OAM             | SXM6                | SXM6                |
| TDP                    | 1000 W          | 1400 W          | 1000 W              | 1300 W              |
| FP32 FLOPs             | 144 TFLOPS      | 157.3 TFLOPS    | 80 TFLOPS           | —                   |
| FP16 FLOPs             | 2.3 PFLOPS      | 2.5 PFLOPS      | 2.25 PFLOPS         | 2.25 PFLOPS         |

*All FLOPs are given without sparsity - no idea why these vendors insist on giving 2:1 sparsity figures.*

Memory capacity and bandwidth will now be on par, and compute numbers seem slightly better for FP16.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/hotchips_amd_scaleup.png)

*Source: AMD*

Their more scientific session was on the design of scale-up fabrics, where they discussed the effects that scale-up switch radix and device lane counts have on the size of the scale-up domain and its bandwidth. Of course, anyone can deduce that more links is better but AMD stressed that scale-up domains should be kept as a single-tier network. They proposed a 1.5 layer network that mitigates some of the issues described in the slides below too, which was quite interesting. More details in [Zartbot's article](https://mp.weixin.qq.com/s?__biz=MzUxNzQ5MTExNw==&mid=2247494795&idx=1&sn=7d61581ee737601bbfd8c5669c15873d&chksm=f849b6ffdd62bb7a24d5265998bebc65559c2d7a8a0ec18dc76ebe51b344c26c0251a423617b&xtrack=1&scene=90&subscene=93&sessionid=1756156201) on day 0 of HotChips 25.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/hotchips_amd_1.5tier.png)

*Source: AMD*

### Meta: Catalina pod (NVL36x2)

One of the major issues with NVL72 systems when they were first announced was how few datacentres could at the time support such high power racks and how few could ever even hope to adapt their infrastructure to support them in the future. The NVL72 rack-scale form factor remains a non-starter for the majority of datacentres around the world, as most places support between 12 or 20kW per rack. This includes Meta, who have a lot of datacentre space designed for CPU servers and low-power MTIA accelerators.

But for training their foundation models, Meta would prefer the raw bandwidth of the 72-GPU NVLink scale-up domain instead of the 8-GPU domain bounded by a chassis for HGX type servers. This, as well as other reasons, led them to customise the system to the extent that it became six racks.

The ["Catalina" pod](https://wccftech.com/meta-catalina-pod-couples-nvidia-blackwell-gb200-nvl72-open-rack-v3-liquid-cooling/) - a [six-rack system](https://www.datacenterdynamics.com/en/news/how-meta-acheives-120kw-a-rack-in-20kw-air-cooled-data-centers/) designed to support 120kW of TDP over 6 x 20kW racks - brings 2 racks of 18 custom GB200 trays together with 18 NVLink switch trays to form a single 72-GPU domain. Four of the six racks are dedicated just to the cooling systems: air-assisted liquid cooling, using the large volume available of four standard width racks to keep liquid coolant temperatures down using fans.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/hotchips_meta_rack.png)

*Source: Meta*

To this extent, they had to customise the trays to have 2 GPUs per tray instead of the usual 4 in a GB200 compute tray, making the ratio of CPU:GPU = 1:1. This then doubles the number of CX-7 NICs and Grace CPUs per GPU, leading to some very interesting specs:

- 72 B200 GPUs and 72 Grace CPUs
- 34.6TB aggregate LPDDR5X memory
- 48TB aggregate cache-coherent memory (CPU-GPU unified memory)
- 14.4TB/s aggregate Scale-out bandwidth

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/hotchips_meta_tray.png)

*Source: Meta*

One issue we believe Meta works around is the lack of power headroom here, with the total system being restricted to 120kW with little or no push beyond that. Combined with the fact that the number of CPUs, NICs, NVLink switches, and many other components have actually increased in number due to this setup, this will likely lead to throttling of the GPUs clock rates to stay within the 120kW envelope.

### Intel: Clearwater Forest CPU

Earlier this year [we reported](https://sixrackunits.substack.com/i/169948586/the-surprising-mystery-of-diamond-rapids-leaked-tdp) on leaks regarding Intel's upcoming Diamond Rapids CPU, their "P-core" only processor aimed at high performance AI/HPC clusters. The counterpart to the "rapids" series of CPU is the "forest" series, aimed at more scalable and less intensive workloads like virtualisation, hosting, databases and so on. For their upcoming Clearwater Forest CPU, Intel decided to go with an official reveal.

The below image summarises the specs for a dual-socket setup, so halve the quantities (except the UPI) for a single-socket setup. Though knowing the target market of these CPUs, a single-socket setup may be unlikely, as virtualisation and web/app hosting servers are supposed to be as core-dense and energy efficient as possible.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/hotchips_intel_cpu.png)

*Source: Intel*

For more information, [Zartbot's article](https://mp.weixin.qq.com/s?__biz=MzUxNzQ5MTExNw==&mid=2247495152&idx=2&sn=d7e5c25374bcddaf3e302c27d7436dee&chksm=f882c3aebffeb63a3e0950965af5cdee93f030fc7958cfa650daf449e5954dcfc2ef887013d2&xtrack=1&scene=90&subscene=93&sessionid=1756236875) on WeChat and [Andreas Schilling's article](https://www.hardwareluxx.de/index.php/news/hardware/prozessoren/66880-hot-chips-2025-intel-nennt-weitere-details-zur-clearwater-forest.html) on HardwareLUXX are very detailed.

### Others

There were also great sessions from names like d-Matrix, Rebellions, Marvell, Huawei, and more, but we wont cover them in this newsletter.

## B300 GPU finally detailed

Also unveiled at HotChips 25 but given its own segment here, the [B300 "Blackwell Ultra" GPU](https://developer.nvidia.com/blog/inside-nvidia-blackwell-ultra-the-chip-powering-the-ai-factory-era/) makes headlines even though most of the information given here was already known for months. We have a few details now though worth noting:

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/b300_arch.jpg)

*Source: Nvidia*

- 288GB HBM3E is implemented as 8 stacks, probably at 12hi, totalling 8TB/s
- 20,480 CUDA cores, and 160 streaming multiprocessors (SMs), which total to 640 5th gen Tensor cores
- Over 160MB of tensor memory (TMEM), the same volume of L1 data cache (shared mem), and L2 cache size unknown

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/b300_sm.webp)

*Source: Nvidia*

For more practical-minded people, the B300 sticks to the current generations 128GB/s unidirectional PCIe 6.0 x16 H2D connection, even though PCIe 6.0 CPUs or SSDs don't exist yet. PCIe 6.0 NICs, however, do exist, such as the [ConnectX-8 SuperNIC](https://resources.nvidia.com/en-us-accelerated-networking-resource-library/connectx-datasheet-c) with an integrated PCIe 6.0 switch. This marks a [fundamental change](https://developer.nvidia.com/blog/nvidia-connectx-8-supernics-advance-ai-platform-architecture-with-pcie-gen6-connectivity/) in the server architecture for HGX's going forward, as GPUs now connect to the NICs at a 2:1 ratio instead of to discrete PCIe switches. This makes their connection to the scale-out network 1 hop shorter and also gives the GPUs a real chance to saturate the 800G uplinks. As for TDP, the peak of 1400W remains the same.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/b300_server.png)

*Source: Nvidia*

Earlier this year, Nvidia developed the [NVFP4 floating point format](https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/) for efficient, stable, and accurate FP4 inference. The B300 delivers up to 1.5x the performance of the B200 for this format, but this is likely theoretical as actual NVFP4 quantised model inferencing numbers (tokens or samples per second) haven't been given yet. The majority of inferencing provided by foundation model labs as AI models or wrapped text or image generation services in other products may still happen on H100s and H200s though for a while. B300 customers investing in this hardware may do so for inferencing the largest models or for future proofing for the next year or two, or, most likely, training. This means that for many, NVFP4 performance numbers are irrelevant.

## Yet another switch from Broadcom - scaling across with Jericho4

Scale-up and scale-out are both rapidly developing dimensions for device-device communications, though now we're beginning to see the limits of how far they can actually scale. Limits enforced not by the technology itself, but from cooling, power, and space constraints.

Racks, and even rows of racks can only get so big before the distance is too great for a larger scale out domain. [Signal integrity and power](https://www.silicon-line.com/copper-cable-limitations/) become too difficult to manage beyond a few meters and taking scale-up to the optical domain is incredibly expensive. Though in certain markets like China, [Huawei is showing](https://semianalysis.com/2025/04/16/huawei-ai-cloudmatrix-384-chinas-answer-to-nvidia-gb200-nvl72/#scale-up-optics-and-no-copper) that this might not be a roadblock to adoption.

Beyond that, scale-out can cover the span of a whole datacentre with a relatively high-bandwidth fabric, but after a certain scale, switch and optics costs become difficult to justify. Clusters like [xAI's Colossus](https://www.theregister.com/2024/10/29/xai_colossus_networking/) are pushing that boundary by doubling the size of the domain to 200,000 GPUs whilst keeping everything under a single scale-out ethernet fabric.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/jericho_chip.png)

*Source: Broadcom*

Enter Broadcom, with the 51.2T [Jericho4](https://investors.broadcom.com/news-releases/news-release-details/broadcom-ships-jericho4-enabling-distributed-ai-computing-across) "Across DC scale-out" ASIC. Aimed at long-range connections between scale-out fabrics (scale-out used synonymously with datacentre here), the Jericho4 includes many features that optimise for transport at these distances whilst maintaining a secure and lossless fabric.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/jericho_scaleacross.png)

*Source: Broadcom*

The main standout innovation that Broadcom advertise is the Hyperport - 4 x 800G links combined at the hardware-level into a single logical 3.2T port. This then reduces the associated overheads of managing 4 distinct ports too. This functionality has already existed for a while at the software layer with link aggregation (LAG) but Hyperport implements it lower in the stack, optimising the load balancing, congestion control, utilisation, and more.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/jericho_ports.jpeg)

*Source: Broadcom*

In addition, the Jericho4:

- Has deep buffers to absorb bursty traffic from AI workloads
- Supports lossless connections for over 100km distances
- Provides MACsec at line rate, necessary for long-distance traffic

And just to future proof it for use in 2027/28, the Jericho4 is also UEC compliant - interoperable with all other UEC switches and NICs from any vendor.

This then "completes" Broadcom's lineup of high-performance AI cluster switch ASICs, with this chip joining the Tomahawk 6 and Tomahawk Ultra to cover all three dimensions of network scaling: up, out, and across. For more information on the Tomahawk series, see our [June](https://sixrackunits.substack.com/i/167217145/broadcom-shows-the-world-a-terabit-switch-asic-tomahawk) and [July](https://sixrackunits.substack.com/i/169948586/broadcoms-inevitable-yet-surprising-new-chip-tomahawk-ultra) editions.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/jericho_lineup.jpeg)

*Source: Broadcom*

PS: It seems they'll do anything to avoid just saying "scale-across", perhaps to avoid association with Nvidia's Spectrum-XGS announcement (more on that just above)? Or maybe they were just a few days short to coining the term?

## PCIe 8.0 announced

Intel and AMD's next generation CPUs - supporting PCIe (Peripheral Component Interconnect express) 6.0 - are [expected to ship](https://www.pcworld.com/article/2805679/pci-express-6-products-might-finally-ship-in-2025.html) between 4Q25 and 4Q26, likely being followed closely by the corresponding SSDs, NICs, and more. PCIe 6.0 itself however was announced as early as 1Q22, resulting in a wait of over 3.5 to 4.5 years from announcement to implementation. Based on the pace so far demonstrated, future PCIe generations should take just as long to reach the market from their reveal. But there's been one fundamental addition to the world driving hardware progression to speeds not seen before: LLMs.

Keeping to their commitment to doubling bandwidth every 3 years, the PCI-SIG (Special Interest Group) [has announced PCIe 8.0](https://pcisig.com/pci-sig-announces-pcie-80-specification-targeted-release-2028), aiming for up to 1TB/s bi-directional bandwidth over a full x16 connection. Version 1.0 of the specification is expected to be released in 2028, with the first devices hopefully shipping before 2032. In comparison, [PCIe 7.0](https://pcisig.com/pcie-70-specification-now-available-pci-sig-members) was announced in 2022, aims to have it's version 1.0 ratified at the end of 2025, and may see adoption in devices as soon as 4Q26. Certainly not CPUs, but possibly in NICs (already reaching 800G and soon 1.6T), and just maybe in SSDs (if storage arrays and controllers reach those speeds in time).  

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/august/images/pcie8_speeds.jpg)

*Source: PCI-SIG*

To summarise what these speeds mean, PCIe 8.0 is targeting 256GT/s (Giga Transfers per second) bidirectional (both transmitting and receiving simultaneously) per lane. [A lane](https://www.techradar.com/computing/computing-components/pcie-lanes-explained) is four wires, two each for transmitting (Tx) and receiving (Rx) and each pair is a [differential pair](https://en.wikipedia.org/wiki/Differential_signalling). A transfer is 2 bits, since PCIe 8.0 will use [PAM4](https://blog.samtec.com/post/understanding-nrz-and-pam4-signaling/) (pulse amplitude modulation with 4 levels) signalling. This means 512Gb/s per lane, or 64GB/s per lane, and therefore a x16 (full width) connection can support 16 x 64GB/s = ~1TB/s bi-directional bandwidth.

---

## Other notable headlines

* [Jensen Huang confirms that GTC Washington DC will reveal the Rubin GPUs as well as five other chips](https://www.tweaktown.com/news/107259/nvidia-ceo-to-visit-tsmc-in-taiwan-first-ever-gtc-in-washington-d-c-for-rubin-ai-gpu-reveal/index.html)
* [SK-Hynix to mass produce 2Tb 3D QLC NAND devices, on the path towards 244TB SSDs](https://www.tomshardware.com/pc-components/ssds/sk-hynix-announces-mass-production-of-its-2tb-3d-qlc-nand-cheaper-high-capacity-consumer-drives-and-244tb-enterprise-ssds-incoming)
* [Rumours of Nvidia's post-Rubin "Feynman" GPUs needing immersion cooling abound from industry sources](https://zdnet.co.kr/view/?no=20250818162633)
* [Samsung's HBM4 samples reportedly pass Nvidia's validation! A turnaround for Samsung in the HBM market finally?](https://m.sedaily.com/NewsView/2GWP8QI6ZB)
* [Huawei allegedly working on "AI SSDs" to reduce pressure on the Chinese HBM supply chain](https://finance.sina.cn/2025-08-25/detail-infnfiew2224904.d.html?vt=4&cid=76524&node_id=76524)
* [AMD might reveal "Venice" 6th gen CPUs and the MI500X at their upcoming financial analyst day in November](https://www.tomshardware.com/pc-components/cpus/amd-to-disclose-roadmaps-in-mid-november-the-future-of-zen-6-rdna-cdna-and-udna-expected)
* [UltraRAM, tech that could store data for up to 1000 years, at DRAM speeds, is progressing towards manufacturing](https://www.tomshardware.com/pc-components/ram/ultraram-scaled-for-volume-production-memory-that-promises-dram-like-speeds-4-000x-the-durability-of-nand-and-data-retention-for-up-to-a-thousand-years-is-now-ready-for-manufacturing)
* [Nvidia announces the RTX Pro 4000 SFF and RTX Pro 2000 GPUs - Desktop grade, aimed at HPC and visualisation workloads](https://www.tomshardware.com/news/nvidia-announces-rtx-pro-4000-sff-and-rtx-pro-2000-desktop-gpus)
* [Delays in DeepSeek's R2 model allegedly due to pressure from Chinese government, being forced to use Huawei's "unstable" AI accelerators instead of Nvidia GPUs](https://www.tweaktown.com/news/107116/huawei-pressure-blamed-for-deepseeks-next-gen-ai-model-delay/index.html)
* [Kioxia confirms that they are also in the race to HBF with their prototype: 5TB capacity @ 64GB/s per "module"...](https://www.kioxia.com/en-jp/about/news/2025/20250820-1.html)
* [...But SanDisk keeps up the pace by teaming up with SK-Hynix to work on standardising HBF first](https://mp.weixin.qq.com/s?chksm=c2649258f5131b4e3fa13fdac3fe6d57db83ce5e0c0a34af6ad4da969da2e1ef27add8bf5c24&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1754993167_1&mid=2247526353&sn=c8250c005cc42ad5f79a630f6a1115c6&idx=3&__biz=MzkzMTcxODM3NA%3D%3D&scene=169&subscene=200&sessionid=1754993168)
* [Meta working with Broadcom to get "Santa barbara" codenamed MTIA servers into production by end of 2025](https://www.datacenterdynamics.com/en/news/meta-places-order-for-its-next-gen-asic-powered-ai-servers-partners-with-broadcom-and-quanta-computer/)
* [Leaks of a possible Jaguar shores thermal test vehicle reveal a possible quad-die arrangement for Intel's last chance at the GPU market](https://wccftech.com/intel-next-gen-ai-chip-jaguar-shores-test-vehicle-surfaces-online/)
* [Japan's FugakuNEXT Supercomputer will use upcoming Fujitsu Monaka CPUs with Nvidia GPUs, adopting NVFusion tech](https://blogs.nvidia.com/blog/fugakunext/)

---

[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)