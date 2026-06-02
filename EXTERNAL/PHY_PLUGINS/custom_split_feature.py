"""Show how to write a custom split action."""

from phy import IPlugin, connect
import numpy as np
from sklearn.cluster import KMeans, MeanShift, SpectralClustering
from sklearn.mixture import GaussianMixture
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


def _uniq(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


class ExampleCustomSplitFeaturePlugin(IPlugin):
    def attach_to_controller(self, controller):
        @connect
        def on_gui_ready(sender, gui):
            @controller.supervisor.actions.add(
                submenu="Clustering",
                shortcut="s",
                prompt=True,
                n_args=5,
                # prompt_default=lambda: [139,1,133,1,2],
            )
            def kmeans(chan1, comp1, chan2, comp2, n_clusters):
                """Split using the K-means clustering: channel1 pc1 channel2 pc2 nclusters"""

                # Selected clusters across the cluster view and similarity view.
                cluster_ids = controller.supervisor.selected

                # Get the amplitudes, using the same controller method as what the amplitude view
                # is using.
                # Note that we need load_all=True to load all spikes from the selected clusters,
                # instead of just the selection of them chosen for display.

                print("Selected channels = ", chan1, chan2)
                channel1 = np.where(controller.model.channel_mapping == chan1)[0]
                channel2 = np.where(controller.model.channel_mapping == chan2)[0]
                m1 = controller._get_features(cluster_ids[0], channel1, load_all=True)
                m2 = controller._get_features(cluster_ids[0], channel2, load_all=True)

                a1 = m1.data[:, :, comp1 - 1]
                a2 = m2.data[:, :, comp2 - 1]

                a_comb = np.concatenate((a1, a2), axis=1)
                # a_comb = StandardScaler().fit_transform(a_comb)
                km = KMeans(n_clusters=int(n_clusters)).fit(a_comb)
                labels = km.labels_

                # We get the spike ids and the corresponding spike template amplitudes.
                # # NOTE: in this example, we only consider the first selected cluster.
                spike_ids = m1.spike_ids
                # y = bunchs[0].amplitudes

                # # We perform the clustering algorithm, which returns an integer for each
                # # subcluster.
                # labels = k_means(y.reshape((-1, 1)))
                assert spike_ids.shape == labels.shape

                # # We split according to the labels.
                controller.supervisor.actions.split(spike_ids, labels)

        @connect
        def on_gui_ready(sender, gui):
            @controller.supervisor.actions.add(
                submenu="Clustering",
                shortcut="z",
                prompt=True,
                n_args=4,
                # prompt_default=lambda: [139,1,133,1,2],
            )
            def mean_shift(chan1, comp1, chan2, comp2):
                """Split using mean_shift algorithm: channel1 pc1 channel2 pc2 nclusters"""

                # Selected clusters across the cluster view and similarity view.
                cluster_ids = controller.supervisor.selected

                # Get the amplitudes, using the same controller method as what the amplitude view
                # is using.
                # Note that we need load_all=True to load all spikes from the selected clusters,
                # instead of just the selection of them chosen for display.

                print("Selected channels = ", chan1, chan2)
                channel1 = np.where(controller.model.channel_mapping == chan1)[0]
                channel2 = np.where(controller.model.channel_mapping == chan2)[0]
                m1 = controller._get_features(cluster_ids[0], channel1, load_all=True)
                m2 = controller._get_features(cluster_ids[0], channel2, load_all=True)

                a1 = m1.data[:, :, comp1 - 1]
                a2 = m2.data[:, :, comp2 - 1]

                a_comb = np.concatenate((a1, a2), axis=1)
                labels = MeanShift(bandwidth=2).fit_predict(a_comb)

                # We get the spike ids and the corresponding spike template amplitudes.
                # # NOTE: in this example, we only consider the first selected cluster.
                spike_ids = m1.spike_ids
                # y = bunchs[0].amplitudes

                # # We perform the clustering algorithm, which returns an integer for each
                # # subcluster.
                # labels = k_means(y.reshape((-1, 1)))
                assert spike_ids.shape == labels.shape

                # # We split according to the labels.
                controller.supervisor.actions.split(spike_ids, labels)


class ReclusterGaussian(IPlugin):
    def attach_to_controller(self, controller):
        # self.manual_selection = controller.selection.channel_id

        @connect
        def on_gui_ready(sender, gui):
            @controller.supervisor.actions.add(
                shortcut="b",
                prompt=True,
                n_args=3,
                # prompt_default=lambda: [139,1,133,1,2],
            )
            def gaussian(chan1, chan2, n_clusters):
                """Split using gaussian algorithm: channel1 channel2 nclusters"""
                # manual_selection = []
                # try:
                #     manual_selection.append(controller.selection.channel_id)
                # except:
                #     selected_cluster = controller.supervisor.selected
                #     best_chans = controller.get_best_channels(selected_cluster[0])
                #     manual_selection.append(best_chans[:2])

                # Selected clusters across the cluster view and similarity view.
                cluster_ids = controller.supervisor.selected
                # selected_channels = controller.get_best_channels(cluster_ids[0])

                # Get the amplitudes, using the same controller method as what the amplitude view
                # is using.
                # Note that we need load_all=True to load all spikes from the selected clusters,
                # instead of just the selection of them chosen for display.
                # chan1, chan2 = self.channel_ids[:2]
                print("Selected channels = ", chan1, chan2)
                # chan1, chan2 = selected_channels[:2]
                channel1 = np.where(controller.model.channel_mapping == chan1)[0]
                channel2 = np.where(controller.model.channel_mapping == chan2)[0]
                m1 = controller._get_features(cluster_ids[0], channel1, load_all=True)
                m2 = controller._get_features(cluster_ids[0], channel2, load_all=True)

                a1 = m1.data[:, :, :].squeeze()
                a2 = m2.data[:, :, :].squeeze()

                a_comb = np.concatenate((a1, a2), axis=1)

                labels = GaussianMixture(n_components=n_clusters).fit_predict(a_comb)
                # labels = model.predict(a_comb)

                # We get the spike ids and the corresponding spike template amplitudes.
                # # NOTE: in this example, we only consider the first selected cluster.
                spike_ids = m1.spike_ids
                # y = bunchs[0].amplitudes

                # # We perform the clustering algorithm, which returns an integer for each
                # # subcluster.
                # labels = k_means(y.reshape((-1, 1)))
                assert spike_ids.shape == labels.shape

                # # We split according to the labels.
                controller.supervisor.actions.split(spike_ids, labels)


class NoisyPeriodSpikes(IPlugin):
    def attach_to_controller(self, controller):
        # self.manual_selection = controller.selection.channel_id

        @connect
        def on_gui_ready(sender, gui):
            @controller.supervisor.actions.add(
                shortcut="alt+q",
                prompt=True,
                n_args=2,
                # prompt_default=lambda: [139,1,133,1,2],
            )
            def noisy_period_spikes(t1, t2):
                """Isolate spikes between: t1 t2"""

                cluster_id = controller.supervisor.selected[0]

                # get spike frames
                spike_ids = controller.model.get_cluster_spikes(cluster_id)
                spike_times = controller.model.spike_times[spike_ids]
                # spike_ids = controller._get_features(cluster_id[0], load_all=True)

                noisy_bool = np.where((spike_times > t1) & (spike_times < t2), 1, 0)

                # separate noisy spikes into separte cluster
                controller.supervisor.actions.split(spike_ids, noisy_bool)

        @connect
        def on_gui_ready(sender, gui):
            @controller.supervisor.actions.add(
                shortcut="alt+r",
                prompt=True,
                n_args=2,
                # prompt_default=lambda: [139,1,133,1,2],
            )
            def noisy_period_spikes_from_all(t1, t2):
                """Isolate spikes from all clusters between: t1 t2"""

                clu_ids = np.unique(controller.model.spike_clusters)
                spike_times_all = controller.model.spike_times

                for clu in clu_ids:

                    # get spike frames
                    spike_id_clu = controller.model.get_cluster_spikes(clu)
                    spike_times_clu = spike_times_all[spike_id_clu]
                    # spike_ids = controller._get_features(cluster_id[0], load_all=True)

                    noisy_bool = np.where(
                        (spike_times_clu > t1) & (spike_times_clu < t2), 1, 0
                    )

                    if sum(noisy_bool) > 0:
                        # separate noisy spikes into separte cluster
                        controller.supervisor.actions.split(spike_id_clu, noisy_bool)
                        print(clu, "done")

        @connect
        def on_gui_ready(sender, gui):
            @controller.supervisor.actions.add(shortcut="alt+i")
            def VisualizeShortISI():
                """Split all spikes with an interspike interval of less than 1.5 ms into a separate
                cluster. THIS IS FOR VISUALIZATION ONLY, it will show you where potential noise
                spikes may be located. Re-merge the clusters again afterwards and cut the cluster with
                another method!"""

                # logger.info('Detecting spikes with ISI less than 1.5 ms')

                # Selected clusters across the cluster view and similarity view.
                cluster_id = controller.supervisor.selected[0]
                spike_ids = controller.get_spike_ids(cluster_id)
                spike_times = controller.get_spike_times(cluster_id)

                dspike_times = np.diff(spike_times)
                labels = np.ones(len(dspike_times), "int64")
                labels[dspike_times < 0.0015] = 2
                labels = np.append(
                    labels, 1
                )  # include last spike to match with len spike_ids

                assert spike_ids.shape == labels.shape

                # We split according to the labels.
                controller.supervisor.actions.split(spike_ids, labels)
                # logger.info('Splitted short ISI spikes from main cluster')


class OutlierDetection(IPlugin):
    def attach_to_controller(self, controller):
        def _detect(method="isolation_forest"):
            cluster_ids = controller.supervisor.selected
            cluster_data = controller._get_features(cluster_ids[0], load_all=True)

            features = cluster_data["data"]
            features = features.reshape(features.shape[0], -1)

            if method == "isolation_forest":
                labels = IsolationForest(random_state=0).fit_predict(features)
                labels[labels == -1] = 2  # negative labels are not acceptable in phy

            spike_ids = cluster_data["spike_ids"]
            assert len(spike_ids) == len(labels)

            # split according to the labels.
            controller.supervisor.actions.split(spike_ids, labels)

        @connect
        def on_gui_ready(sender, gui):
            @controller.supervisor.actions.add(submenu="Outlier", shortcut="shift+o")
            def isolation_forest():
                """Outlier"""
                _detect("isolation_forest")

