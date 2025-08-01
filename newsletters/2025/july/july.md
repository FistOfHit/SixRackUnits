[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# July 2025

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/title.jpeg)

*How would we even measure the compute speed of something like this? Even for modern digital processors, measuring actual INTOPS or FLOPS is difficult and sometimes meaningless.*

This is the SixRackUnits AI hardware newsletter, keeping you up to date with the latest in AI hardware, datacentre technology, and the future of compute. With a field changing this fast, staying on top and even summarising all the material available can be difficult - so we do it for you.

For a space to share sources and news/updates, join our telegram channel <a href="https://t.me/aihpc_infra_fans">here</a> or if you like short form posts on similar topics,check out the <a href="https://sixrackunits.substack.com/notes">notes</a> section of this newsletter or my <a href="https://www.linkedin.com/in/hitesh-kumar58">LinkedIn</a>.

[**This month's updates:**](#this-months-updates)
  - [**Broadcom's inevitable yet surprising new chip - Tomahawk Ultra**]()
  - [**GB300 servers possibly shipping before 4Q25, "no major issues" allegedly**]()
  - [**The surprising mystery of Diamond rapids' leaked TDP**]()
  - [**H20 GPU orders pile in - Nvidia (and AMD) gains access to China again**]()
  - [**Other notable headlines**]()

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

- Nvidia keeping the same motherboard design from GB200s (Bianca) after numerous issues with rushing the new design
- Original Cordelia board design was 4 B300 ultras with 2 Grace, but there were persistent issues signal loss traced back to the SXM socket interface. Now using bianca sxm puck instead, they can reuse the supply chain and experience. 
- GB300 can now be adopted and made faster as they are re-using existing components
- Nvidia no longer supplying the full board themselves, instead  
- there have been reports of liquid cooling system issues with leaks with the GB200s so far
- worst part are the quick connect fittings
- B300 itself will be in the SXM puck (easily replaceable) and the grace CPU will still come in a seperate BGA package
- Ball grid array soldering vs SXM puck style
- VR upgrade will be in two parts - not stressing the supply chain and customers too much: VR inside Oberon NVL144, then VR inside Kyber NVL576

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/gb300_rack.jpg)

*Source: ServeTheHome*

Mass production is now underway for GB300 servers with [initial shipments expected in September](https://money-udn-com.cdn.ampproject.org/c/s/money.udn.com/money/amp/story/5612/8839283) for some of the largest customers. Volumes will peak in 4Q25 and continue into 2026, with Foxconn being the primary supplier and Wiwynn, Inventec, and Wistron being the others - All of which are Taiwanese. These aren't the first Blackwell Ultra systems in deployment though, as [CoreWeave and Dell](https://www.servethehome.com/dell-and-coreweave-show-off-first-nvidia-gb300-nvl72-rack/) famously deployed the worlds first GB300 NVL72 at the start of this month, likely the first sample version publicly announced.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/gb300_boards.jpg)

*Source: Alethia Capital*

This timely ramp up of shipments comes as news to some because in Q2 it was reported that there may be delays in GB300 shipments due to technical issues with the memory and 

There hasn't been any update on what, if anything, Nvidia and their supply chain have done to address the liquid cooling issues that have been [rumoured in the GB200s](https://mp.weixin.qq.com/s?chksm=fbc55528ccb2dc3e97dbf3ac94f65e3f0065a467d80a2bb8dc0fa3128f0d2f3207b8d5326653&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1752912746_1&mid=2247486037&sn=c25851920d412e008b1ed65d22e9c3ff&idx=1&__biz=MzU1NjUwMTUyMg%3D%3D&scene=169&subscene=200&sessionid=1752912745&flutter_pos=13&clicktime=1752912771&enterid=1752912771&finder_biz_enter_id=5&jumppath=20020_1752912748097%2CWebViewStubProxyUI_1752912749788%2C20020_1752912749904%2C50094_1752912758176&jumppathdepth=4&ascene=56&fasttmpl_type=0&fasttmpl_fullversion=7825680-en_US-zip&session_us=gh_6c32bda7f91f) in deployment currently. It seems that the quick connect fittings used to speed up the deployment and maintenance of the servers have been the primary cause .

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/gb300_tray.png)

*Source: Asus*






---

## The surprising mystery of Diamond rapids' leaked TDP

[The first leak](https://x.com/x86deadandback/status/1941808014865899878) was posted early this month on X from the account @x86deadandback, and drew mixed reactions from the hardware community. It provided some specs of Intel's upcoming server-grade CPU series, Diamond Rapids (DMR) (successor to the current gen. Granite rapids (GNR) series), which is expected to be formally announced in the next few months. The source themselves isn't a well established industry leaker, but the numbers given for the are believable and match expectations.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/intel_specs.jpeg)

*Source: @x86deadandback on X*

For context, the [highest performing Intel GNR SKU](https://www.intel.com/content/www/us/en/products/sku/240777/intel-xeon-6980p-processor-504m-cache-2-00-ghz/specifications.html) is advertised at 500W for 128 cores running at 2GHz base clock, and rumours suggest AMD's nex gen. ["Venice" 192 (virtual) core CPU](https://www.guru3d.com/story/amd-6thgen-epyc-venice-ccd-configuration-and-thread-performance-spotted/) will reach 600W. If the higher end AI/HPC server Intel CPUs reach 192 cores, then they will still be very competitive with their counterparts from AMD in 2026. [An earlier leak](https://x.com/x86deadandback/status/1937563563935084826) from the same source showed what appeared to be a product page or documentation specifying heat-sinks for DMR CPUs, peaking at 660W. Heat-sinks typically are rated for significantly higher output than the heat source is capable of to manage temporary performance boosts or cooling system failures, and so this specification supports the later leak.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/intel_heatsink.jpeg)

*Source: @x86deadandback on X*

To demonstrate why a 500W TDP would be so surprising, lets walk through an example server upgrade process. Even without the leak, its certain that a four-socket version of DMR will be available for CPU-dense datacentres running in-memory databases, high-performance scientific workloads, or financial transaction processing. For a site using 4096 cores spread over 64 older 64-core 350W [Emeralds rapids CPUs](https://en.wikipedia.org/wiki/Emerald_Rapids), their power usage would be 22.4kW spread over 16 quad-socket servers in two 12kW racks. To keep the minimum core count after an upgrade to DMR CPUs, that site could now buy just 22 new 192-core 500W CPUs in 6 servers, using a total of 11kW only. This could now fit into one of their 12kW racks, with capacity left for a switch or two, and the site overall has now reduced its total power usage by 11.4kW.

The example is oversimplified of course but the concept remains true: newer CPUs are generally more power efficient, and a lower TDP for the same core count can result in power, space, and cost savings if the short-term tradeoffs are acceptable. This decision is a lot easier to make when the TDP of a 192-core CPU is 500W rather than 650W. Combining this with PCIe 6.0 and CXL 3.0 support, variants with 16 memory channels, and upgraded AMX (Advanced Matrix Extensions) support [1](https://www.techradar.com/pro/want-a-quad-socket-server-with-768-cores-sure-intels-192-core-diamond-rapids-xeon-cpu-will-deliver-that-in-2026-but-i-wonder-whether-it-will-be-too-little-too-late), Intel CPUs may soon halt AMDs aggressive takeover of the server CPU market.

There's a lot more information currently circulating around the DMR series and the future of Intel CPUs in general, but they are beyond the scope of this article. For more information, see the following (perhaps more reliable) sources:
- [Discussions around Intel's statement on returning to SMT, and if DMR will also not have it](https://morethanmoore.substack.com/p/intel-ceo-letter-to-employees)
- [Another leak alleging that the DMR architecture will have shared L2 caches per core pairs](https://x.com/InstLatX64/status/1948734994798567678)

---

## H20 GPU orders pile in - Nvidia (and AMD) gains access to China again

Wednesday 16th July marked [Jensen Huang's third visit](https://www.digitimes.com/news/a20250715PD201/nvidia-jensen-huang-rtx-us-china-trade-war-2025.html?chid=10) to China in a very short span of time. This was the first formal announcement that hardware export restrictions have been eased, allowing Nvidia's H20s to be sold in China again. H20s are the second generation of watered down H100 chips, designed to meet the enhanced restrictions imposed on compute capability and bandwidth. Interestingly, by reducing the compute capability, lowering the TDP, and keeping the same number of stacks of HBM as the H100 did, the H20s could actually provide [higher device memory bandwidth](https://semianalysis.com/2023/11/09/nvidias-new-china-ai-chips-circumvent/) (via higher memory clock rates) than the H100s could.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/h20_board.png)

*Source: Nvidia*

When the H20s were originally banned for sale, Nvidia had to write off its existing inventory of ~600-700K H20 GPUs as a [loss of ~$10.5B](https://x.com/Jukanlosreve/status/1947075312694722707?t=syNSPYJTvzyoZZ6IcXFz9w&s=09). Now with the April export controls lifted, Nvidia is expecting to recover that loss and potentially make even more from the increase in demand since then. To this end, Nvidia has already placed an order of over [300K H20 GPUs from TSMC](https://www.reuters.com/world/china/nvidia-orders-300000-h20-chips-tsmc-due-robust-china-demand-sources-say-2025-07-29/), though its expected that there wont be enough supply of HBM to meet this demand and instead Nvidia will [likely use GDDR6 instead](https://x.com/Jukanlosreve/status/1945652728795136033?t=9lBAsHca2W5IssU0XtQVAw&s=0). Even with the reduction in performance that comes with that, it's almost certain that demand will not decrease.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/h20_specs.jpg)

*Source: VideoCardz*

In addition, they've introduced multiple variants of existing GPUs from the western market as well as more SKUs specifically for the Chinese market. For a larger coverage of the cost vs performance space, Nvidia are persisting with the [RTX Pro 6000D](https://www.digitimes.com/news/a20250715PD201/nvidia-jensen-huang-rtx-us-china-trade-war-2025.html) (increasingly called the [B30 now](https://www.tweaktown.com/news/106517/nvidias-new-b30-ai-gpu-planned-to-ship-in-q4-10-20-slower-than-h20-but-30-40-cheaper/index.html?utm_source=newsletter&utm_campaign=newsletter)) announced earlier this year, as well as inferencing only cards such as [the L20 and L2](https://www.tomshardware.com/pc-components/gpus/new-nvidia-ai-gpus-designed-to-get-around-us-export-bans-come-to-china-h20-l20-and-l2-to-fill-void-left-by-restricted-models) which may end up seeing similar success to the L40s for lighter inferencing and graphics workloads. For the retail consumer market, the [5090Dv2 desktop GPU](https://www.tweaktown.com/news/106572/nvidias-new-geforce-rtx-5090-v2-launches-in-china-on-august-12-24gb-vram-600w-tdp/index.html?utm_source=newsletter&utm_campaign=newsletter) will address high-end gaming and graphics workloads, but may end up being seen in lower-tier datacentres just as the infamous RTX 4090 did (and still is). AMD has also had their [MI308 approved](https://www.bloomberg.com/news/articles/2025-07-15/amd-says-it-will-restart-mi308-sales-to-china-after-us-review), and are also persisting with more economic [Radeon AI PRO R9700](https://www.techpowerup.com/337484/amds-export-friendly-radeon-ai-pro-r9700-gpu-prepares-for-china-debut) they announced earlier this year.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/july/images/h20_mi308.png)

*Source: AMD*

This combination of sudden hardware diversity and availability has been met with mixed reactions from industry. It's great for Chinese big tech firms, cloud service providers, and world-leading AI labs who have all been increasingly desperate for infrastructure. Compared to their American and European competition, Chinese AI services providers like Deepseek have had to provide [far lower performance](https://techzephyr.substack.com/p/implications-of-h20-coming-back?triedRedirect=true) in terms of tokens per second. And this is in spite of their necessity-driven research into more efficient inferencing software and model architectures.

The incredible demand has resulted in all sorts of workarounds from building infrastructure via [western neoclouds](https://www.bloomberg.com/news/articles/2025-04-28/coreweave-rival-nscale-seeks-bytedance-deal-and-2-7-billion-in-debt-and-equity?embedded-checkout=true) to [smuggling hardware](https://wccftech.com/nvidia-gb200-ai-servers-are-reportedly-being-smuggled-into-china/) via various APAC countries, predominantly Singapore. One solution is also buying and using domestic GPUs, but this change of hardware availability across the performance vs cost space might now hurt some of these domestic manufacturers who were technically less capable but might otherwise have taken advantage of the lack of supply.

What the locals can do though is focus on systems-level solutions, a space that Nvidia and AMD are and will always be forbidden enter. The prime example that made headlines and is widely regarded as a viable and China-appropriate is Huawei's [CloudMatrix384](https://semianalysis.com/2025/04/16/huawei-ai-cloudmatrix-384-chinas-answer-to-nvidia-gb200-nvl72/), a multi-rack cluster out-performing (on paper) Nvidia's GB200 NVL72s. As we saw at the WAIC25 conference, other Chinese vendors are following suit with preparing and showcasing seemingly well-designed systems.

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
* [SK-Hynix confirms 3GB GDDR7 modules in development](https://www.tomshardware.com/pc-components/gpus/sk-hynix-confirms-3gb-gddr7-memory-modules-are-in-the-works-higher-capacity-could-pave-the-way-for-fabled-rtx-50-series-super-cards-with-24gb-vram)
* [Samsung awared $16B contract for Tesla's AI6 2nm chips over 8 years](https://www.theregister.com/2025/07/22/tesla_ai6_2nm_chip_contract/)

---

[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)