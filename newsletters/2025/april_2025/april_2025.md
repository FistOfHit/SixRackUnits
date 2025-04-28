[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png)](https://sixrackunits.substack.com)

# April 2025

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/title.jpeg)

*Will we ever move away from cables? What could high-bandwidth, low-error, and secure wireless communications looks like in the future?*

[**This month's updates:**](#this-months-updates)
  - [**SemiAnalysis on AMD's upcoming rack-scale SKUs**](#semianalysis-on-amds-upcoming-rack-scale-skus)
  - [**Tenstorrent announces the BlackHole AI accelerator**](#tenstorrent-announces-the-blackhole-ai-accelerator)
  - [**IBM's z17 mainframe**](#ibms-z17-mainframe)
  - [**Ironwood: Google's seventh gen. TPU**](#ironwood-googles-seventh-gen-tpu)
  - [**China's answer to the NVL72 - Huawei's CloudMatrix 384**](#chinas-answer-to-the-nvl72---huaweis-cloudmatrix-384)
  - [**Other notable headlines**](#other-notable-headlines)

[**Vendor spotlight:**](#vendor-spotlight)
  - [**Kove**](#kove)

[**One-pagers:**](#one-pagers)
  - [**Bandwidth and latency**](#bandwidth-and-latency)
  - [**Liquid cooling plates**](#liquid-cooling-plates)

For a space to share sources and news/updates, join on <a href="https://t.me/aihpc_infra_fans">Telegram</a>, and check out my <a href="https://www.linkedin.com/in/hitesh-kumar58">LinkedIn</a> for posts on similar topics!

---

# This month's updates:

## SemiAnalysis on AMD's upcoming rack-scale SKUs

*For AI accelerator manufacturers targeting hyperscalers, few things in AI hardware have become clearer in the past quarter than the need to focus now on systems rather than chips. Nvidia have taken the lead by supplying their NVL rack-scale products to all major hyperscalers as well as some GPUaaS providers, promising a turnkey infrastructure solution that meets the demands of the largest AI workloads. Rumours surface now of AMD's entry into this space with their own, the IF64 and IF128.*

Reported exclusively by [SemiAnalysis](https://semianalysis.com/2025/04/23/amd-2-0-new-sense-of-urgency-mi450x-chance-to-beat-nvidia-nvidias-new-moat/#mi450x-infinity-fabric-over-ethernet-ifoe-ifoe64-mi450x-ifoe128-%e2%80%93-semianalysis-estimates), AMD's IF64 and IF128 are likely to be the names of their rack-scale systems built around the MI450X GPUs, scheduled for 2H26. Competing directly with Nvidia's Rubin "Ultra" GPus (also scheduled for the same time frame), the MI450X 

## Tenstorrent announces the BlackHole AI accelerator

*American RISC chip/server design startup Tenstorrent seeks to take space in both the enterprise and retail AI accelerator markets with its low-power and easy to use PCIe card lineup, as well as servers designed around density and scaling. Their latest card, the BlackHole, seeks to offer a competitive price/performance ratio with a scale-up potential that appears to be significantly greater than what other PCIe devices from competitors such as Google and AWS can offer.*

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/tenstorrent_blackhole.png)

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/tenstorrent_galaxy.png)

## IBM's z17 mainframe

*IBM mainframes are known for their near perfect uptime and low-latency for critical operations such as transaction processing, airline fleet management, and fraud detection to name a few. As more and more such workloads begin to use computationally expensive AI models, IBM's mainframes need to adapt to not just be better at what they already do, but also be better at the workloads of the near-future.*

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/ibm_z17.png)

## Ironwood: Google's seventh gen. TPU

*In 2Q24 Google introduced the "Trillium" TPUv6 (Tensor processing unit), a continuation of their remarkably power-efficient series of custom AI accelerators available on GCP (Google cloud platform). Now, the series continues but with an unexpected progression: Inference and training are no-longer being assigned to two different versions in the same generation. The "Ironwood" TPUv7 appears to take on both workloads but the marketing around it confuses many.*

Google's latest in their custom silicon for AI workloads, the "Ironwood" TPUv7 has just been [announced](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/). It's unclear yet what stage of production it's at, or when it will be generally available for public GCP users, but some specs are available now. Of all the information provided, the most controversial statement made was a misguided (or even dishonest) comparison between a TPU "pod" and the worlds most computationally capable supercomputer, [El Capitan](https://www.top500.org/system/180307/).

The "[Top500](https://www.top500.org/)" organisation maintains a list of the worlds most powerful supercomputers ranked by their performance in a linear algebra benchmark, [Linpack](https://www.netlib.org/benchmark/hpl/). El capitan, placing first as of 4Q24, combines over 43,000 AMD MI300A APUs (CPU + GPU on the same package) to achieve a real performance of 1.74 exaFLOPs at FP64, with a theoretical peak at 2.74. TPUv7 pods on the other hand use their 2 or 3-dimensional torus network topology to combine 9,216 chips (not devices) into a single computational domain and the performance per chip provided in the announcement is a theoretical peak as opposed to a measured benchmark, and is very likely for FP8 or FP16 as opposed to FP64. Google's claim therefore of reaching a 24x advantage in exaFLOPs over El Capitan has been received poorly by analysts with opinions generally skewing towards it being grossly misleading.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/tpuv7.png)

Focusing on the chip itself, it appears that the v7 is a natural successor to the [v5p](https://cloud.google.com/blog/products/ai-machine-learning/introducing-cloud-tpu-v5p-and-ai-hypercomputer), the "performant" version of the 5th generation which aimed to handle both lighter inferencing workloads as well as AI model training use cases, (in contrast to the v5e or "efficient") rather than the [v6](https://cloud.google.com/blog/products/compute/introducing-trillium-6th-gen-tpus) which was likely focused on inferencing only. Finally, looking at the specs ([1](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/) [2](https://www.theregister.com/2025/04/10/googles_7thgen_ironwood_tpus_debut/) [3](https://www.nextplatform.com/2025/04/09/with-ironwood-tpu-google-pushes-the-ai-accelerator-to-the-floor/) [4](https://xpu.pub/2025/04/16/google-ironwood/)):

* 4614 TFLOPs at FP8 (~2300 BF16)
* 192GB HBM at 7.2TB/s - likely 6 stacks of [Micron's 12hi HBM3E](https://www.micron.com/products/memory/hbm/hbm3e#:~:text=Micron's%20HBM3E%20delivers%20pin%20speed,using%20a%2012%2Dhigh%20stack.)
* Likely 4 (possibly 6) ports of ICI at 1.2TB/s bidirectional
* ICI domain size of 9216, possibly in a 96x96 2D torus or 32x32x9 3D torus 
* 4 x 256x256 MXU (systolic arrays), providing 65536 MACs/cycle
* Estimates of up to ~1kW per chip

## China's answer to the NVL72 - Huawei's CloudMatrix 384

*Nvidia's NVL72 was not the first but was certainly the most popular rack-scale, self-contained infrastructure solution built around AI accelerators. Densely packing this volume of high-powered chips into a single rack and interconnecting them with the NVLink scale-up network led to a product that could be easily integrated and used by hyperscalers and large businesses. But the NVL72 has its flaws, and Huawei is stepping up to take on Nvidia in this space too.*

It's likely to come as a surprise to many who don't operate in the Chinese market, but Nvidia internally see Huawei as one of their [biggest competitors](https://semianalysis.com/2025/04/23/amd-2-0-new-sense-of-urgency-mi450x-chance-to-beat-nvidia-nvidias-new-moat/#recommendations-to-nvidia) for AI accelerators. We reported back in [February](https://sixrackunits.substack.com/i/158104265/huaweis-ascend-series) and even last [October](https://sixrackunits.substack.com/i/156730584/huaweis-ascend-c) about Huawei's progress in high-performance AI accelerators, with their Ascend 910C being announced and now mass produced for use in firms such as Baidu, ByteDance, and famously, DeepSeek all evaluating the chips in hopes of beginning to taper off of their reliance on foreign hardware amidst increasingly hostile export policies from the US. 

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/cloudmatrix384_picture.jpeg)

Seeing the trend in the market for rack-scale systems, Huawei have announced their own reference architecture, the [CloudMatrix (CM) 384](https://semianalysis.com/2025/04/16/huawei-ai-cloudmatrix-384-chinas-answer-to-nvidia-gb200-nvl72/), a multi-rack system built around the Ascend 910C AI accelerators and "[CloudEngine](https://carrier.huawei.com/en/products/fixed-network/b2b/ethernet-switches/dc-switches)" network switches. The 16-rack, 384 chip SKU hosts 4 x 8-GPU air-cooled servers per rack over 12 racks with 4 racks of switches, and is fully optically connected for its single scale-up domain; this means that unlike the NVL72 which uses copper for its NVLink scale-up network, the CM384 uses almost 5400 400G transceivers. Some analysts predict this fact alone will limit the number of CM384s that will ever be deployed as its possible that the [supply of transceivers](https://x.com/ResearchQf/status/1916580472706195724) will be insufficient to meet the demand for the racks, rather than the cost or power of these optics. Other's raise concerns about the total power draw of the system, predicted to be at ~560-600kW per unit, well over 3x the advertised power of the NVL72, though SemiAnalysis calculations show an advantage regardless in the FLOPs/Watt ratio of the CM384 over the NVL72.

As for the system's specs:


![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/cloudmatrix384_diagram.png)

## Other notable headlines

* [SK-Hynix possibly mass producing both HBM4 and HBM4E this year](https://www.tweaktown.com/news/104464/sk-hynix-confirms-both-hbm4-and-hbm4e-memory-are-coming-this-year-for-next-gen-ai-gpus/index.html)
* [Chinese firms place up to $16 billion of orders for Nvidia's CHIPS act-dodging AI GPUs](https://www.reuters.com/technology/chinese-firms-place-16-billion-order-new-nvidia-chips-information-reports-2025-04-02/)
* [Samsung reportedly begins developing its 1nm "dream" process, ready for mass production in 2029](https://www.trendforce.com/news/2025/04/10/news-samsung-reportedly-begins-1nm-process-development-targets-2029-mass-production/)
* [Nubis communications and Amphenol to develop signal re-drivers to enable 200G/lane SERDES across multiple meters of copper, enabling multi-rack scale-up networks without optics](https://www.businesswire.com/news/home/20250326861856/en/CORRECTING-and-REPLACING-Nubis-Extends-Linear-Paradigm-from-Optics-to-Copper-with-Breakthrough-Nitro-Linear-Redriver-Solution-Enabling-4-Meter-Reach-for-200Gbps-per-Lane-Copper-Cables-in-AI-Scale-Up-Networks)
* [UALink (Ultra Accelerator Link) consortium announces their 1.0 specification, at 200G per lane. Aims to provide an open standard against Nvidia's NVLink](https://ualinkconsortium.org/)
* [Cadence reveals its HBM4 IP promising up to 12.8 Gbps per lane - 3.2TB/s over a 2048-wide bus for a single stack](https://www.ctol.digital/news/cadence-launches-128gbps-hbm4-ip-subsystem-for-ai-hpc/)
---

# Vendor spotlight:

## Kove

*Host memory capacity is and has always been the be-all and end-all of large, high-performance workloads, as triggering an OOM error usually causes not just the application and its progress/state to crash, but the entire host. [Kove](https://kove.com/) are a firm working to change this with a solution for remote, software-defined memory (SDM) that approaches the performance of local memory.*

Founded in 2003, American firm Kove has quietly been supplying remote memory solutions to customers who found their workloads constrained not by compute, but by memory capacity. Kove's memory tower system presents as a [rack](https://kove.com/products/kovesdm-memory-tower/) of DRAM enclosures containing some management compute and [high-performance NICs](https://arstechnica.com/sponsored/kove-tackles-the-last-software-defined-technology-memory/), and their [software stack](https://kove.com/products/kovesdm-software/) manages the remote memory and transfers to expose a memory pool that can be defined (configured or managed) entirely by software. With a maximum capacity of up to 256TiB (tebibyte, or 2^40 as opposed to 10^12 bytes) across several memory towers available as one unified address space with the local memory, bandwidth-intensive workloads can be accelerated without needing the compute to be throttled.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/kove_towers.png)

*Source: Viking Enterprise Solutions. Multiple memory towers can be combined in the same network fabric, with the address size being the limiting factor rather than physical space.*

At a high-level, the memory tower works by extending the main memory available to a host machine via network-attached DRAM, rather than adding more channels for DIMMs onto the host baseboard or connecting another board via PCIe. Kove supports [InfiniBand for the data plane](https://www.vikingenterprisesolutions.com/kovesdm-memory-tower/) (with RoCE support in the works) and Ethernet for the control plane, allowing for reasonably easy to manage additional infrastructure in any standard ethernet-managed datacentre with a dedicated and isolated high-performance fabric for the data.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/kove_specs.png)

*Source: Kove.*

As for software, the [management and networking stack](https://kove.com/products/kovesdm-software/) works together to use a host server's local memory as a form of cache (think of it as L4/5), and keeps recently accessed and likely soon to be accessed within the host chassis. Remote memory then is able to serve as a nearly-identical access latency extension of this local cache, as the microseconds of time to RDMA data from the tower to host are likely amortized away by both the large bandwidth available on the network and the access prediction capabilities of the software.

---

# One-pagers:

## Bandwidth and latency

*Bandwidth, being the amount of data transferred within a unit time and latency, being the time taken to complete a transfer of a unit size, these two key measurements in any data transfer are often misunderstood and misrepresented. Even worse, some will simple invert bandwidth and call it latency not realising their lack of consideration for overheads, measurement conditions, and variance, and the damage they do to the science.*

Measuring the performance of transferring data via a connection is usually done with two measurements: bandwidth and latency. 

Bandwidth measures the maximum volume of data that can be transferred through a connection in a given unit of time, and is measured as a rate such as Mbps (megabits per second). It's important to note that this is the maximum theoretical rate, not the actual or "realised" rate of data transfer across a connection. Bandwidth is often abstracted (applied to) or aggregated (accumulated) across a subset or an entirety of a network to give some indication of the potential rate that can be achieved for a workload using it. Latency on the other hand measures the time taken for a minimum unit volume of data to be transferred from a source to a destination, and is measured in units of time such as milliseconds. Some factors that influence latency like distance between endpoints or the speed/path of light in a material are physical and unavoidable, whilst others like the time to encode and decode signals are dependant on the hardware and protocols used for transmission. 

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/bandwidth_latency.png)

A common error made when measuring network performance is assuming that bandwidth is the inverse of latency, i.e. that a bandwidth of 100 Mbps implies a latency of 1/100 seconds. This assumption is ignores a few issues:

* Latency is only measured for a minimal sized transfer, one that should never be large enough to saturate a link for measuring bandwidth
* Bandwidth does not include the overheads involved with each minimal transfer, as these are amortized away when sending data in volume
* As the rate of transfer over w channel increases, so does contention and hence resource utilisation, which causes an increase in latency i.e. the relationship is non-linear

## Liquid cooling plates

*The height of air-cooled AI servers is influenced significantly by the size of the fans and the height of the heatsinks required to keep high-powered accelerator hardware cool. Compression attached cooling plates replace tall towers of metal fins in thinner-profile servers where getting enough airflow for cooling kilowatt+ devices either costs double-digit percentages of the servers total power draw, or is just physically impossible.*

A prime example of air cooling pushed to its limits is SuperMicro's B200 HGX server, the [SYS-A22GA-NBRT](https://www.supermicro.com/en/products/system/gpu/10u/sys-a22ga-nbrt). Fitting 8 Nvidia B200 GPUs (each with a TDP of 1200W) as well as 2 Intel Xeon 6900s (about 500W each) into an air cooled chassis requires accommodating the cooling fin towers for the GPUs, taking up the entire floor-space in the chassis as well as over 6U of height. The remaining space needs to be large enough so that enough airflow can pass to keep the other components such as CPUs, NICs, SSDs and more. Pushing beyond this limit to 1400W+ TDP chips and more will require significantly greater volumes of airflow moving through impractically large chassis, to the point where the power used by cooling fans will creep towards 15 or even 20% of the servers total draw.

![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/newsletters/2025/april_2025/images/coolit_plate.png)

Using a denser fluid such as liquid is the next logical step for cooling systems. Immersion cooling appears to still be building a reputation, having been only applied successfully in a very small number of setups, and so the only practical solution currently is direct-to-chip liquid cooling. In this paradigm, large coolant distribution units (CDUs) are placed underneath or at the side of existing racks and large, high pressure plumbing systems connect the pumps to in/outlets on the chassis. Further plumbing internal to the chassis then routes the cooled liquid from the CDU through "cold plates", or flat hollow plates made from copper or aluminum, which are in placed in contact with the chips/components. The heated liquid is then pumped back to the CDU for cooling. 

Systems like the plate shown above can reliably cool chips with TDPs of up to 2000W, with models rated for 4000W (under very high coolant pressures) being evaluated for future AI accelerators. For servers, adopting cooling plates for all or even some of the components leads to a significant increase in power efficiency and compute density, allowing for solutions like Nvidia's NVL72 racks. Definitely not the first - but by far the most popular - NVL72s use extensive liquid cooling support infrastructure to cool 27 x 1U trays in a single rack, requiring many types of cooling plates for the various collections of components on the baseboard. Moving forward, more standard server architectures are likely to shrink in size towards 2-4U and datacentre PUE values will decrease. 



[![](https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png)](https://sixrackunits.substack.com)