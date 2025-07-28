[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# July 2025

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/title.jpg)

**

This is the SixRackUnits AI hardware newsletter, keeping you up to date with the latest in AI hardware, datacentre technology, and the future of compute. With a field changing this fast, staying on top and even summarising all the material available can be difficult - so we do it for you.

For a space to share sources and news/updates, join our telegram channel <a href="https://t.me/aihpc_infra_fans">here</a> or if you like short form posts on similar topics,check out the <a href="https://sixrackunits.substack.com/notes">notes</a> section of this newsletter or my <a href="https://www.linkedin.com/in/hitesh-kumar58">LinkedIn</a>.

[**This month's updates:**](#this-months-updates)
  - [**Broadcom's inevitable yet surprising new chip - Tomahawk Ultra**]()

---

# This month's updates:

## Broadcom's inevitable yet surprising new chip - Tomahawk Ultra

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/broadcom_chip.png)

*Source: Broadcom*

Announced just weeks after the 102.4T Tomahawk 6, the [new Tomahawk Ultra ASIC](https://investors.broadcom.com/news-releases/news-release-details/broadcom-ships-tomahawk-ultra-reimagining-ethernet-switch-hpc) is symbolic of Broadcom's scale-up Ethernet (SUE) overtaking UALink as the scale-up technology most capable of challenging Nvidia's NVLink. The 51.2T (512 x 100G) switch expands the performance and capability boundaries of Broadcom's existing datacentre switch lineup, with its focus on lower latencies and higher packet processing rates as well as supporting SUE's requirements such as link-layer retry and credit-based flow control.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/broadcom_ultra.webp)

*Source: Broadcom (via WeChat)*

The key number that marketing have decided to lead with is the switching latency - 250ns. It's an impressive number considering that this number for Tomahawk 5 may have been [double that](https://www.wheelersnetwork.com/2025/07/broadcom-adds-new-architecture-with.html?m=1). It should be noted however that this is purely the latency incurred from when a unit of data enters the ASIC to when it exits, and not the more important latency of getting a message from one device to another. That number still relies on other factors such as the size and priority of the message being sent, the design of the rest of the switch chassis, and any intermediate hardware such as NICs, PCIe switches, and even cable lengths for particularly long connections. This means that in or near the worst cases for latency (usually the bottlenecks for real workloads), even on the highest performing clusters, this reduction in switching latency might not make a significant difference.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/broadcom_latency.png)

*Source: Broadcom (via WeChat)*

The more surprising improvement (and probably more impactful too) though is their packet processing rate. Claiming to process [77 Billion packets per second (pps)](https://www.naddod.com/blog/broadcom-tomahawk-ultra-new-chip-for-scale-up-ethernet), Broadcom are targeting traditional HPC infrastructures too despite the majority of their marketing centering on AI. Applications such as finite difference/element models, linear solvers, or even distributed financial/trading programs are all far more sensitive to latency than AI workloads are. This has been the case for AI training for a while now, where packet sizes are usually large enough to saturate deep-buffers in higher-tier switches, and is now the norm in inferencing too, which has become almost entirely about LLMs. As a result, HPC clusters using more dense and complex topologies will benefit greatly from the high pps provided by the Tomahawk Ultra.

These dramatic performance improvements mean that the architecture of the chip has had to change a lot. The addition of more packet-processing pipelines to meet the pps requirements and compute logic to support the in-network collectives (INC) that SUE supports has resulted in the buffers needing to be smaller - and shallower - than they were in the Tomahawk 5.  As a result of all of these changes, it's technically [not really a "Tomahawk" chip anymore](https://www.wheelersnetwork.com/2025/07/broadcom-adds-new-architecture-with.html?m=1), despite its compatibility with existing sockets/boards. This doesn't - and shouldn't - matter to most though, and Broadcom's decision to label and market this chip as being in the same family as their scale-out ASICs makes complete sense.

---

## GB300 servers possibly shipping before 4Q25, "no major issues" allegedly

---

## JEDEC releases the LPDDR6 standards, samples potentially out by 4Q25

---

## The surprising mystery of Diamond rapids' leaked TDP
 [](https://www.techpowerup.com/338664/intel-diamond-rapids-xeon-cpu-to-feature-up-to-192-p-cores-and-500-w-tdp)
- DMR doesnt have SMT [source](https://x.com/InstLatX64/status/1948734994798567678)
- 500W TDP seems suspiciously low, unsure if thats for a mid-spec version or for the 192 core version
- Granite rapids reaches 500W TDP, peaks at 128 cores at 2.0GHz [](https://en.wikipedia.org/wiki/Granite_Rapids), and is restricted to a two socket version. This one says a 4s version. There must be some caveats here or restrictions for being only 500W TDP. 
- In comparison AMD TUrin CPUs hit 192 cores already within a 500W envelope [](https://en.wikipedia.org/wiki/Epyc), and rumours are that Venice will hit 600W at a much lower core count [](https://wccftech.com/amd-zen-6-epyc-venice-zen-6-cpus-256-cores-2026-epyc-verano-zen-7-instinct-mi500-gpus-2027/)
- Supports up to 16 channels of DDR5, and can also support MRDIMMs, a new form factor that is more dense and high bandwidth. 
- Also PCIe 6.0 and CXL 3.0. 

- Interesting they come in 4 socket configs, which are quite rare in practice. Given the core counts, 2 socket servers will remain the primary choice for high-performance deployments in both CPU management or virtualisation servers and for accelerator-focused servers like HGX-like deployments. 
- 4s version implies up to 768 cores per server in a 2kW envelope, great for consolidation and upgrades - for example, if you had to replace all of your ~1500 cores in a CPU rack containing older emeralds rapids [](https://en.wikipedia.org/wiki/Emerald_Rapids), youd have to replace 12 servers of 2 x 64-core of high end 8592+s, using a total power of 8.4kW, with 4 servers of 2 x 192-core DMRs, which use a total of 4kW. Instantly creating 4.4kW out of nowhere for other new equipment.

- comments on the post say it'll be higher TDPs like 750w but this also might be a but much. AMD venice 256 core might not even reach that high

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/intel_specs.jpeg)

---

## H20 GPU orders pile in - Nvidia (and AMD) gains access to China again

- H20 has started selling in china again
- Specs:


- AMD also got approval for the MI308 for china
- Specs: 

---

## Other notable headlines

* [Samsung may supply HBM4 samples to AMD, Nvidia, and others by end of this month...](https://mp.weixin.qq.com/s?__biz=MzUzNTI5MTg3NA==&mid=2247485277&idx=1&sn=87490e5877da966181e0b765783bd76b&poc_token=HLOWgmijKey9o-fT9lAP_wGWGOj-DZZtaBWvlD0f)
* [...But mass production may end up starting in 2026 after all](https://www.digitimes.com/news/a20250724PD223/samsung-hbm4-production-2026-sk-hynix.html#:~:text=Report%20SCMP%20Bundle-,Samsung%20delays%20HBM4%20rollout%20to%202026%20due%20to%20yield%20challenges,strengthens%20lead%20in%20AI%20memory&text=Samsung%20Electronics%20is%20reportedly%20pushing,amid%20ongoing%20DRAM%20redesign%20efforts.)
* [NVidia brining CUDA to RISC-V machines - but maybe RISC CPUs only, not GPUs](https://xpu.pub/2025/07/23/cuda-risc-v/)
* [Huawei to display the CloudMatrix384 in person, live, at the end of this month at WAIC25](https://money.udn.com/money/story/5603/8882141)
* [Against all odds, smugglers find a way to get GB200 racks into China - on sale now](https://www.tweaktown.com/news/106623/nvidia-gb200-ai-servers-smuggled-into-china-despite-their-two-ton-weight/index.html)
* [HBM4 is coming](https://www.hbm4.org/)
* [Tesla to use TSMC for its Dojo 3 chip](https://www.ctee.com.tw/news/20250725700068-430501)
* [Intel's next-gen desktop CPUs, "Titan Lake" possibly scrapping P/E-core split, moving to unified cores](https://www.trendforce.com/news/2025/07/18/news-intel-reportedly-drops-hybrid-architecture-for-2028-titan-lake-go-all-in-on-100-e-cores/)
* [Huawei may move to a more GPU-like architecture for the future of its Ascend series AI accelerators](https://x.com/kyleichan/status/1943879673382867403?t=_jO4qxORFtzyS6FsfP6Zpw&s=09)
* [AI accelerator startup Furiosa wins a significant customer in Korea - LG Electronics](https://www.theregister.com/2025/07/22/sk_furiosa_ai_lg/)
* []()

---

[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)